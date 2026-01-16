import flet as ft
import random

def main(page: ft.Page):
    page.title = "Do You Love Me?"
    page.window_width = 450
    page.window_height = 800
    page.bgcolor = "#2c2c2e"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # دوال الحركة والنجاح
    def move_no(e):
        # كبرنا مساحة الحركة حتى ينهزم بكل مكان بالكارد
        btn_no.top = random.randint(20, 500)
        btn_no.left = random.randint(20, 250)
        btn_no.update()

    def show_success(e):
        # بدلاً من مسح الصفحة، راح نغير محتوى الكارد نفسه
        white_card.content = ft.Column([
            ft.Image(src="success.gif", width=250),
            ft.Text("I knew it! 🥰", size=30, color="black", weight="bold"),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        white_card.update()

    # عناصر واجهة السؤال
    main_img = ft.Image(src="start.gif", width=200)
    question_text = ft.Text("Do you love me?", size=22, weight="bold", color="black")
    
    btn_yes = ft.ElevatedButton(
        "Yes", 
        bgcolor="#4cd964", 
        color="white", 
        width=100, 
        on_click=show_success # استدعاء دالة النجاح
    )

    btn_no = ft.Container(
        content=ft.ElevatedButton("No", bgcolor="#ff3b30", color="white", width=100),
        top=400,  
        left=130,
        animate_offset=ft.Animation(300, ft.AnimationCurve.EASE_OUT_BACK) 
    )
    btn_no.on_hover = move_no
    btn_no.content.on_click = move_no

    # الكارد الأبيض اللي يحتوي كل شيء
    white_card = ft.Container(
        content=ft.Stack([
            ft.Column([
                main_img,
                question_text,
                ft.Row([btn_yes], alignment=ft.MainAxisAlignment.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20, width=350, height=600),
            btn_no
        ]),
        bgcolor="white",
        width=350,
        height=600,
        border_radius=30,
        padding=10,
    )

    page.add(
        ft.Text("Do You Love Me?", size=30, weight="bold", color="white"),
        ft.Container(height=10),
        white_card
    )

ft.run(main, assets_dir="assets")