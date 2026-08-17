from django import forms
from .models import Room, Bed, Student, Rent, Food, Expense
from django.db import models


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        exclude = ['available_beds']

        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-select'}),
            'sharing_type': forms.Select(attrs={'class': 'form-select'}),
            'total_beds': forms.NumberInput(attrs={'class': 'form-control'}),
            'monthly_rent': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'college': 'College / Workplace',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhaar': forms.TextInput(attrs={'class': 'form-control'}),
            'college': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'room': forms.Select(attrs={'class': 'form-select'}),
            'bed': forms.Select(attrs={'class': 'form-select'}),
            'food_type': forms.Select(attrs={'class': 'form-select'}),
            'deposit': forms.NumberInput(attrs={'class': 'form-control'}),
            'joining_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:

            self.fields["bed"].queryset = Bed.objects.filter(
                models.Q(status="Vacant") |
                models.Q(pk=self.instance.bed_id)
            )

        else:

            self.fields["bed"].queryset = Bed.objects.filter(
                status="Vacant"
            )


class RentForm(forms.ModelForm):

    class Meta:

        model = Rent

        fields = [
    "student",
    "month",
    "year",
    "monthly_rent",
    "late_fine",
    "paid_amount",
    "payment_date",
    "payment_mode",
    "transaction_id",
    "collected_by",
    "status",
    "remarks",
]

        widgets = {

            'student': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'month': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'year': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'monthly_rent': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'late_fine': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'paid_amount': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'payment_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'payment_mode': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'transaction_id': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'collected_by': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'status': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'remarks': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),

        }

        # exclude = (
        #     'receipt_number',
        #     'total_amount',
        #     'pending_amount',
        # )

class FoodForm(forms.ModelForm):

    class Meta:

        model = Food

        exclude = (
            'breakfast_cost',
            'lunch_cost',
            'dinner_cost',
            'total_cost',
            )

        widgets = {

            'student': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'food_type': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'breakfast_cost': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'lunch_cost': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'dinner_cost': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'remarks': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
        }

class ExpenseForm(forms.ModelForm):

    class Meta:

        model = Expense

        fields = '__all__'

        widgets = {

            'expense_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'category': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'amount': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'payment_mode': forms.Select(
                attrs={'class': 'form-select'}
            ),

            'paid_to': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),

        }

        exclude = (
            'receipt_number',
        )