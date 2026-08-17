from django.db import models
from django.utils import timezone
from string import ascii_uppercase


# ==========================================
# Room Model
# ==========================================

class Room(models.Model):

    ROOM_TYPE = (
        ('A/C', 'A/C'),
        ('Non A/C', 'Non A/C'),
    )

    SHARING_TYPE = (
        ('2 Sharing', '2 Sharing'),
        ('3 Sharing', '3 Sharing'),
        ('4 Sharing', '4 Sharing'),
    )

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE)
    sharing_type = models.CharField(max_length=20, choices=SHARING_TYPE)

    total_beds = models.PositiveIntegerField()
    available_beds = models.PositiveIntegerField(default=0)

    monthly_rent = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):

        is_new = self.pk is None

        if is_new:
            self.available_beds = self.total_beds

        super().save(*args, **kwargs)

        # Create beds only when the room is first created
        if is_new:

            for i in range(self.total_beds):

                Bed.objects.create(
                    room=self,
                    bed_number=f"Bed {i + 1}"
                )

    def __str__(self):
        return self.room_number


# ==========================================
# Bed Model
# ==========================================

class Bed(models.Model):

    STATUS_CHOICES = (
        ('Vacant', 'Vacant'),
        ('Occupied', 'Occupied'),
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='beds'
    )

    bed_number = models.CharField(max_length=20)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Vacant'
    )

    class Meta:
        unique_together = ('room', 'bed_number')

    def __str__(self):
        return f"{self.room.room_number} - {self.bed_number}"


# ==========================================
# Student Model
# ==========================================

class Student(models.Model):

    FOOD_CHOICES = (
        ('Veg', 'Veg'),
        ('Non Veg', 'Non Veg'),
    )

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Left', 'Left'),
    )

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    aadhaar = models.CharField(max_length=12)

    college = models.CharField(
        max_length=150,
        verbose_name="College / Workplace"
    )

    address = models.TextField()

    photo = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )

    bed = models.OneToOneField(
        Bed,
        on_delete=models.CASCADE
    )

    food_type = models.CharField(
        max_length=20,
        choices=FOOD_CHOICES
    )

    joining_date = models.DateField(
        default=timezone.now
    )

    deposit = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    def save(self, *args, **kwargs):

        is_new = self.pk is None

        if not is_new:
            old_student = Student.objects.get(pk=self.pk)

            if old_student.bed != self.bed:

                old_student.bed.status = "Vacant"
                old_student.bed.save()

                old_student.room.available_beds += 1
                old_student.room.save()

        super().save(*args, **kwargs)

        self.bed.status = "Occupied"
        self.bed.save()

        self.room.available_beds = self.room.beds.filter(
            status="Vacant"
        ).count()

        self.room.save()

    def __str__(self):
        return self.name


class Rent(models.Model):

    MONTH_CHOICES = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )

    PAYMENT_MODE = (
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Debit Card', 'Debit Card'),
        ('Credit Card', 'Credit Card'),
        ('Cheque', 'Cheque'),
    )

    PAYMENT_STATUS = (
        ('Paid', 'Paid'),
        ('Partial', 'Partial'),
        ('Pending', 'Pending'),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='rents'
    )

    month = models.CharField(
        max_length=20,
        choices=MONTH_CHOICES
    )

    year = models.PositiveIntegerField(default=2026)

    monthly_rent = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    late_fine = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        editable=False,
        default=0
    )

    paid_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    pending_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        editable=False,
        default=0
    )

    payment_date = models.DateField(default=timezone.now)

    payment_mode = models.CharField(
        max_length=30,
        choices=PAYMENT_MODE
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    receipt_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    collected_by = models.CharField(
        max_length=100,
        default="Admin"
    )

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Paid"
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):

        self.total_amount = self.monthly_rent + self.late_fine
        self.pending_amount = self.total_amount - self.paid_amount

        if not self.receipt_number:

            last = Rent.objects.order_by('-id').first()

            if last:
                number = last.id + 1
            else:
                number = 1

            self.receipt_number = f"RCPT{number:05d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.month}"

class Food(models.Model):

    FOOD_TYPE = (
        ('Veg', 'Veg'),
        ('Non Veg', 'Non Veg'),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='foods'
    )

    date = models.DateField(default=timezone.now)

    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)

    food_type = models.CharField(
        max_length=20,
        choices=FOOD_TYPE
    )

    breakfast_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    lunch_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    dinner_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    total_cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        editable=False
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):

        if self.breakfast:
            self.breakfast_cost = 50
        else:
            self.breakfast_cost = 0

        if self.lunch:
            self.lunch_cost = 100
        else:
            self.lunch_cost = 0

        if self.dinner:
            self.dinner_cost = 80
        else:
            self.dinner_cost = 0

        self.total_cost = (
            self.breakfast_cost +
            self.lunch_cost +
            self.dinner_cost
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.date}"
    


class Expense(models.Model):

    CATEGORY_CHOICES = (

        ('Electricity', 'Electricity'),
        ('Water', 'Water'),
        ('Wi-Fi', 'Wi-Fi'),
        ('Gas', 'Gas'),
        ('Cleaning', 'Cleaning'),
        ('Maintenance', 'Maintenance'),
        ('Salary', 'Salary'),
        ('Food Purchase', 'Food Purchase'),
        ('Other', 'Other'),

    )

    PAYMENT_MODE = (

        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Card', 'Card'),

    )

    expense_date = models.DateField(default=timezone.now)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_mode = models.CharField(
        max_length=30,
        choices=PAYMENT_MODE
    )

    paid_to = models.CharField(
        max_length=150
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    receipt_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.receipt_number:

            last = Expense.objects.order_by('-id').first()

            if last:
                number = last.id + 1
            else:
                number = 1

            self.receipt_number = f"EXP{number:05d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category} - ₹{self.amount}"