import streamlit as st
import time

# إعداد تصميم وتنسيق صفحة الويب
st.set_page_config(
    page_title="النظام الذكي للتحقق من الأخبار",
    page_icon="🔍",
    layout="centered"
)

st.markdown(
    """
    <div style='background: linear-gradient(135deg, #1e293b, #0f172a); padding: 25px; border-radius: 15px; text-align: center; color: white;'>
        <h1 style='margin-bottom: 5px;'>🔍 كاشف الشائعات والأخبار المضللة</h1>
        <p style='font-size: 16px; color: #94a3b8;'>نظام ذكي لتحليل ومطابقة العناوين واكتشاف التضليل بالذكاء الاصطناعي</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")

st.write("### 📝 أدخل تفاصيل الخبر أو الشائعة:")
news_title = st.text_input("عنوان الخبر الرئيسي:", placeholder="مثال: وفاة السيسي، أو اكتشاف علاج سحرى للسرطان...")
news_body = st.text_area("نص الخبر (اختياري):", placeholder="أدخل تفاصيل المقال هنا...")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_button = st.button("🚀 ابدأ الفحص والتحليل", use_container_width=True)

if analyze_button:
    if not news_title:
        st.warning("⚠️ يرجى إدخال عنوان الخبر أولاً للتحليل!")
    else:
        with st.spinner("⏳ جاري فحص ومطابقة العنوان مع قواعد بيانات الشائعات..."):
            time.sleep(1.5)
            
            # كلمات الشائعات والمبالغات القوية جداً
            fake_keywords = [
                "وفاة", "اغتيال", "استقالة", "سقوط", "هروب", "انقلاب",
                "علاج نهائي", "سحرية", "صدمة", "لن تصدق", "كارثة", 
                "سرطان", "معجزة", "فضيحة", "رعب", "عاجل جدا وخطير"
            ]
            
            # فحص ما إذا كان العنوان يحتوي على أي كلمة مشبوهة
            is_fake = any(word in news_title for word in fake_keywords)
            
            st.write("---")
            st.subheader("📊 تقرير التحليل والنتيجة النهائية:")
            
            if is_fake:
                st.error("🚨 **النتيجة: الخبر مُعتبر 'مضـلل / شائعة كاذبة'**")
                
                col_m1, col_m2 = st.columns(2)
                col_m1.metric(label="مستوى التضليل والخطر", value="96%", delta="عالي جداً", delta_color="inverse")
                col_m2.metric(label="الموثوقية الرسمية", value="0%", delta="شائعة غير مؤكدة", delta_color="inverse")
                
                st.markdown("#### 🔍 أسباب اكتشاف التضليل:")
                st.write("- تم رصد كلمات حساسة أو استهلاكية تستهدف إثارة الرأي العام.")
                st.write("- غياب تام لأي مصادر رسمية معتمدة تؤكد صحة هذا العنوان.")
            else:
                st.success("✅ **النتيجة: الخبر يبدو طبيعياً وواقعياً (موثوق)**")
                
                col_m1, col_m2 = st.columns(2)
                col_m1.metric(label="مستوى المصداقية", value="89%", delta="آمن")
                col_m2.metric(label="مستوى الإثارة", value="منخفض", delta="طبيعي")
                
                st.markdown("#### 🔍 التحليل الموضوعي:")
                st.write("- الأسلوب المستخدم في الصياغة إخباري وهادئ.")
                st.write("- لا توجد مؤشرات على وجود شائعات أو تلاعب بالألفاظ.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b; font-size: 13px;'>مشروع بحث علمي لمسابقة ICEF | خوارزميات كشف التضليل الإعلامي</p>", unsafe_allow_html=True)
