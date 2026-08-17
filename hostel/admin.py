from django.contrib import admin
from .models import Room, Bed, Student, Rent, Food, Expense

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        'room_number',
        'room_type',
        'sharing_type',
        'total_beds',
        'available_beds',
        'monthly_rent'
    )


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):

    list_display = (
        'room',
        'bed_number',
        'status'
    )

    list_filter = (
        'status',
        'room'
    )
    search_fields = (
        'room__room_number',
        'bed_number',
    )

    list_editable = (
        'status',
    )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'room',
        'bed',
        'food_type',
        'status'
    )

    search_fields = (
        'name',
        'phone'
    )

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):

    list_display = (
        'receipt_number',
        'student',
        'month',
        'year',
        'monthly_rent',
        'paid_amount',
        'pending_amount',
        'payment_mode',
        'status',
    )

    list_filter = (
        'month',
        'payment_mode',
        'status',
    )

    search_fields = (
        'receipt_number',
        'student__name',
    )

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'date',
        'food_type',
        'breakfast',
        'lunch',
        'dinner',
        'total_cost',
    )

    list_filter = (
        'date',
        'food_type',
    )

    search_fields = (
        'student__name',
    )

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

    list_display = (

        'receipt_number',
        'expense_date',
        'category',
        'amount',
        'payment_mode',

    )

    list_filter = (

        'category',
        'payment_mode',
        'expense_date',

    )

    search_fields = (

        'category',
        'paid_to',

    )