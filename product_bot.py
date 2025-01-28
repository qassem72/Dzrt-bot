import requests
 from bs4 import BeautifulSoup
  import time
   
    # الرابط إلى صفحة المنتج
     url = "https://example.com/desert-ice-rush"  # ضع هنا رابط صفحة المنتج الفعلي
      
       # الكلمات المفتاحية للمنتج
        keywords = ["دزرت آيسي رش", "Desert Ice Rush"]  # استبدل هذا بالكلمات المناسبة
         
          # دالة لفحص توفر المنتج
           def check_availability():
                    try:
                                 response = requests.get(url)
                                          response.raise_for_status()  # تأكد من أن الاتصال بالموقع ناجح
                                                   soup = BeautifulSoup(response.text, "html.parser")
                                                            
                                                                     # تحليل النصوص من الصفحة
                                                                              page_text = soup.get_text().lower()
                                                                               
                                                                                        # التحقق من وجود الكلمات المفتاحية
                                                                                                 for keyword in keywords:
                                                                                                                  if keyword.lower() in page_text:
                                                                                                                                       print(f"المنتج '{keyword}' متوفر!")
                                                                                                                                                        return True
                                                                                                                                                             print("المنتج غير متوفر حاليًا.")
                                                                                                                                                                  except Exception as e:
                                                                                                                                                                               print(f"خطأ أثناء التحقق: {e}")
                                                                                                                                                                                    return False
                                                                                                                                                                                 
                                                                                                                                                                                 # فحص متكرر كل 10 دقائق
                                                                                                                                                                                  while True:
                                                                                                                                                                                           if check_availability():
                                                                                                                                                                                                        break
                                                                                                                                                                                                         print("إعادة المحاولة بعد 10 دقائق...")
                                                                                                                                                                                                              time.sleep(600)  # انتظار 10 دقائق قبل المحاولة مرة أخرى

