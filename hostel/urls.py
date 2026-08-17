from django.urls import path
from . import views


urlpatterns = [

    # ==========================================================
    # Dashboard
    # ==========================================================

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    # ==========================================================
    # Room Management
    # ==========================================================

    path(
        'rooms/',
        views.room_list,
        name='room_list'
    ),

    path(
        'rooms/add/',
        views.add_room,
        name='add_room'
    ),

    path(
        'rooms/edit/<int:pk>/',
        views.edit_room,
        name='edit_room'
    ),

    path(
        'rooms/delete/<int:pk>/',
        views.delete_room,
        name='delete_room'
    ),

    # ==========================================================
    # Bed Management
    # ==========================================================

    path(
        'beds/',
        views.bed_list,
        name='bed_list'
    ),

    # ==========================================================
    # Student Management
    # ==========================================================

    path(
        'students/',
        views.student_list,
        name='student_list'
    ),

    path(
        'students/<int:student_id>/',
        views.student_detail,
        name='student_detail'
    ),

    path(
        'students/add/',
        views.add_student,
        name='add_student'
    ),

    path(
        'students/edit/<int:pk>/',
        views.edit_student,
        name='edit_student'
    ),

    path(
        'students/delete/<int:pk>/',
        views.delete_student,
        name='delete_student'
    ),

    # ==========================================================
    # Rent Management
    # ==========================================================

    path(
        'rent/',
        views.rent_list,
        name='rent_list'
    ),

    path(
        'rent/add/',
        views.add_rent,
        name='add_rent'
    ),

    path(
        'rent/edit/<int:pk>/',
        views.edit_rent,
        name='edit_rent'
    ),

    path(
        'rent/delete/<int:pk>/',
        views.delete_rent,
        name='delete_rent'
    ),

    path(
        'rent/receipt/<int:pk>/',
        views.payment_receipt,
        name='payment_receipt'
    ),

    # ==========================================================
    # Food Management
    # ==========================================================

    path(
        'food/',
        views.food_list,
        name='food_list'
    ),

    path(
        'food/add/',
        views.add_food,
        name='add_food'
    ),

    path(
        'food/edit/<int:pk>/',
        views.edit_food,
        name='edit_food'
    ),

    path(
        'food/delete/<int:pk>/',
        views.delete_food,
        name='delete_food'
    ),

    path(
        'food/report/',
        views.food_report,
        name='food_report'
    ),

    # ==========================================================
    # Expense Management
    # ==========================================================

    path(
        'expense/',
        views.expense_list,
        name='expense_list'
    ),

    path(
        'expense/add/',
        views.add_expense,
        name='add_expense'
    ),

    path(
        'expense/edit/<int:pk>/',
        views.edit_expense,
        name='edit_expense'
    ),

    path(
        'expense/delete/<int:pk>/',
        views.delete_expense,
        name='delete_expense'
    ),

    # ==========================================================
    # Reports Dashboard
    # ==========================================================

    path(
        'reports/',
        views.reports_dashboard,
        name='reports_dashboard'
    ),

    # ==========================================================
    # Student Reports
    # ==========================================================

    path(
        'reports/students/',
        views.student_report,
        name='student_report'
    ),

    path(
        'reports/students/pdf/',
        views.student_report_pdf,
        name='student_report_pdf'
    ),

    path(
        'reports/students/excel/',
        views.student_report_excel,
        name='student_report_excel'
    ),

    path(
        'reports/students/print/',
        views.student_report_print,
        name='student_report_print'
    ),

    # ==========================================================
    # Room Reports
    # ==========================================================

    path(
        'reports/rooms/',
        views.room_report,
        name='room_report'
    ),

    path(
        'reports/rooms/pdf/',
        views.room_report_pdf,
        name='room_report_pdf'
    ),

    path(
        'reports/rooms/excel/',
        views.room_report_excel,
        name='room_report_excel'
    ),

    path(
        'reports/rooms/print/',
        views.room_report_print,
        name='room_report_print'
    ),

    # ==========================================================
    # Rent Reports
    # ==========================================================

    path(
        'reports/rent/',
        views.rent_report,
        name='rent_report'
    ),

    # ==========================================================
    # Expense Reports
    # ==========================================================

    path(
        'reports/expense/',
        views.expense_report,
        name='expense_report'
    ),

    # ==========================================================
    # Finance Reports
    # ==========================================================

    path(
        'reports/finance/',
        views.finance_report,
        name='finance_report'
    ),

    # ==========================================================
    # Report Center
    # ==========================================================

    path(
        'reports/center/',
        views.report_center,
        name='report_center'
    ),

    # ==========================================================
    # Bed Reports
    # ==========================================================

    path(
        'reports/beds/pdf/',
        views.bed_report_pdf,
        name='bed_report_pdf'
    ),

    path(
        'reports/beds/excel/',
        views.bed_report_excel,
        name='bed_report_excel'
    ),

    path(
        'reports/beds/print/',
        views.bed_report_print,
        name='bed_report_print'
    ),

    # ==========================================================
    # Student Statistics
    # ==========================================================

    path(
        'reports/student-statistics/',
        views.student_statistics,
        name='student_statistics'
    ),

    path(
        'reports/student-statistics/pdf/',
        views.student_statistics_pdf,
        name='student_statistics_pdf'
    ),

    path(
        'reports/student-statistics/excel/',
        views.student_statistics_excel,
        name='student_statistics_excel'
    ),

    path(
        'reports/student-statistics/print/',
        views.student_statistics_print,
        name='student_statistics_print'
    ),

    # ==========================================================
    # Financial Analytics
    # ==========================================================

    path(
        'reports/financial-analytics/',
        views.financial_analytics,
        name='financial_analytics'
    ),

    path(
        'reports/financial-analytics/pdf/',
        views.financial_analytics_pdf,
        name='financial_analytics_pdf'
    ),

    path(
        'reports/financial-analytics/excel/',
        views.financial_analytics_excel,
        name='financial_analytics_excel'
    ),

    path(
        'reports/financial-analytics/print/',
        views.financial_analytics_print,
        name='financial_analytics_print'
    ),

    # ==========================================================
    # Authentication
    # ==========================================================

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'change-password/',
        views.change_password,
        name='change_password'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
]