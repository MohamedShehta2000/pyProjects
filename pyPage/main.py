# استدعاء المكاتب 
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio import config
# https://youtu.be/_iJtrXCdECQ?si=Jx_Hya3k2KCgYL7a
# code css اخر حاجة كتبتها 
#  اول حاجة لينك استايل الخط للعنوان الرئيسي
# # معناها تعريف في السي  اس اس
# 
css = """
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@100;200;300;400;500;600;700&family=Reem+Kufi:wght@400..700&display=swap');
#h3{
font-family: "Reem Kufi", sans-serif;
}
#para{font-family: "Reem Kufi", sans-serif;
color:blue}
#y{width:75%;}
"""
@config(css_style=css)
# بنعرف التطبيق
def app():
    # هنا هنكتب عنوان الصفحة اول ما تدخل 
    put_text ('أهلا بك في عالم محمد شحتة').style('text-align:right;')
    # هنا هنحط صور اللينك- العرض-الارتفاع 
    put_image('https://i.pinimg.com/originals/7e/cc/4e/7ecc4e972cc9d2f40dea8b17f1064776.png', width='1200px', height='200px')
    #  code html h-p-ul-li-details-summery-p-audio-hr p-
    put_html("""
        <h3 id='h3'>أول تطبيق بايثون</h3>
        <p id='para'>اهلا وسهلا بيكم في العالم الاخر</p>
        <ul>
            <li>تعليم البايثون</li>
            <li> تعليم البايثون</li>
            <li>تعليم البايثون</li>
        </ul>
        <details id='y'>
             <summery> الخطة</summery> <p>المسار التعليمي</p>
             <audio controls>
                   <source src="https://server13.mp3quran.net/husr/001.mp3" type="audio/mp3">
             </audio>
             <audio controls>
                   <source src="https://server13.mp3quran.net/husr/001.mp3" type="audio/mp3">
             </audio>
             <hr>
        <p>جميع الحقوق محفوظة@moshehta</p>

    """).style('direction:rtl; text-align:right;')
# السيرفر 
start_server(app, port=34345 , debug=True)
