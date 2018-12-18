# DigiLit

DigiLit is a basic programming tool for doing digital humanities.Its functions include:        
- Find names in the text
- Segment text into chapters,acts, scenes, etc. by input keyword
- Graph a number of names distributions by chapters
- View tokens and numbers by chapters
- View pronoun distributions (1st person, 2nd person, and 3rd person)
- Calculate MEAN, SUM, and PERCENTAGE of each pronoun
- View POS tagged tokens by chapters

## ที่มาและความสำคัญ
ที่มาสำหรับโปรแกรมนี้ คือ ความสนใจส่วนตัวในการศึกษาวรรณกรรม จึงอยากจะประยุกต์วิชานี้เข้ากับสิ่งที่สนใจ แต่ก็ไม่ทราบว่าภาษาศาตร์ใช้ทำอะไรได้บ้าง ผู้พัฒนาจึงพยายามหาว่าภาษาศาสตร์เข้ามามีส่วนในการศึกษางานวรรณกรรมอย่างไร พบว่ามีการใช้คลังข้อมูลเข้ามาศึกษา stylistics หรือ stylometrics ของงานเขียนของนักเขียนว่ามีลักษณะอย่างไร เช่นในงานของVirginia Woolf ว่ามีลักษณะการเขียนอย่างไร ไปจนถึงการพัฒนาการของตัวละคร (Balossi,2014:41-58). หรือในทาง NLP พบว่ามีการใช้ Name Entity Recognitions (NER) เข้ามาในการค้นข้อมูลใหญ่ ๆ จากหลักการการทำงานของทั้งสองอย่าง พบว่าหากสามารถค้นหาชื่อตัวละครและดูว่าแต่ละบทหรือตอนมีชื่อตัวละครใดปรากฎอยู่บ้าง ก็อาจจะช่วยให้เห็นภาพหรือโครงเรื่องได้ชัดเจนขึ้น อีกทั้งการศึกษา POS ก็มีส่วนสำคัญในการวิเคราะห์ lexical density หรือ lexical richness อันสามารถนำไปจัดจำแนกสไตล์การเขียนหรือประเภทงานเขียนได้ จึงนำมาสู่การสร้างโปรแกรมนี้ขึ้นเพื่อเป็นเครื่องมือช่วยในการศึกษาโครงเรื่อง อีกทั้งยังต้องการหาการกระจายตัวและสัดส่วนของคำสรรพนาม เพื่ออาจจะนำไปศึกษาต่อว่า สัมพันธ์กับ POV อย่างไร 

Balossi, Giuseppina._A Corpus Linguistic Approach to Literary Language and Characterization : Virginia Woolf’s The Waves_. John Benjamins Publishing Company, 2014.


## วิธีดำเนินการ

ก่อนดำเนินการ
ศึกษาว่า Name Entity Recognitions มีวิธีการหรือเครื่องมือใดในการทำ
วางแผนว่าต้องการให้งานตนเองออกมาประมาณไหน 

ศึกษาการใช้ NLTK ว่ามีการใช้งาน word_tokenize(), pos_tag(), ne_chunk() FreqDist() ว่าใช้งานอย่างไร
หาข้อมูลtext จาก www.gutenberg.org 
เริ่มเขียนโปรแกรมด้วยการใช้ NLTK เพื่อหาคำที่เป็นคน
พยายามหาวิธีการในการแยกข้อมูลออกเป็นส่วน ๆ ว่าจะทำอย่างไรได้บ้าง  
หลังจากการดำเนินการ พยายามแก้โค้ดให้สั้นลงและจัดให้โค้ดที่ดำเนินการคล้ายกันอยู่ในขั้นตอนเดียวกัน

ศึกษาการใช้ numpy, pyplot, time, sys.stdout, การรวม list, การหาsubsetใน list เป็นต้น

เครื่องมือที่ใช้ในการเขียนโปรแกรมนี้ มีดังนี้
- [NLTK Toolkit](https://www.nltk.org)
- [NumPy](http://www.numpy.org)
- [matplotlib](https://matplotlib.org)
- [PrettyTable](https://pypi.org/project/PrettyTable/)

## ผลการดำเนินการ
จากการดำเนินการ ได้ผลที่พึงพอใจ แม้จะตัดแบ่งบทหรือตอนของเรื่องได้ไม่ตรงนัก แต่ที่ได้ก็สามารถทำให้เห็นโครงเรื่องได้ว่าช่วงใดที่ตัวละคนปรากฏร่วม 
 จะเห็นได้จากตัวอย่างงานที่นำมาศึกษา เช่น Measure for Measure ![im1](https://github.com/Nat-Nimit/raw-data/blob/master/7A476546-D704-414A-9156-27D586A0DEBF.jpeg) หรือในเรื่อง Moby Dick ![im2](https://github.com/Nat-Nimit/raw-data/blob/master/73166E2B-B99B-4E45-9DB2-0CD524A7DD40.jpeg)
นอกจากนี้เมื่อลองดูการกระจายตัวของคำสรรพนาม หรือPOSแล้วพบว่ามีข้อมูลที่น่าศึกษาต่อเช่น สัดส่วนคำสรรพนามกับมุมมองการเล่าเรื่อง เช่นใน Measure for Measure มีสรรพนามบุรุษที่ 2 มากพอกับบุรุษที่ 3 อาจจะเป็นเพราะเป็นบทละครพูด ![im3](https://github.com/Nat-Nimit/raw-data/blob/master/094D63C0-ABE5-4F83-A24E-81AA70465AEA.jpeg) ส่วนใน _Narrative of the Life of Frederick Douglass, an American Slave_ พบรูปแบบที่ต่างออกไป ![im5](https://github.com/Nat-Nimit/raw-data/blob/master/BF33F4CE-F04B-420A-9EA6-AED04BE683DB.jpeg) จะเห็นว่าสรรพนามบุรุษที่สองมีจำนวนน้อยมาก เช่นกันกับสัดส่วน CONTENT WORDS VS FUNCTION WORDS ที่คนเขียนคนเดียวกันแต่มีสัดส่วนที่ต่างกันว่ามีปัจจัยอะไรเข้ามาเกี่ยวข้อง ![im4](https://github.com/Nat-Nimit/raw-data/blob/master/5BD9C92D-3FB2-4D0B-B30F-74A613FA7546.jpeg) จะเห็นได้ว่าตอนต้นกับท้ายมีสัดส่วนที่ต่างออกไป 

## อุปสรรค
ยังไม่คุ้นเคยกับการใช้ class ว่าอะไรควรใช้เป็น subclass ก็เลยสลับไปสลับมาทำให้โค้ดแก้ผิด อีกทั้งเนื่องจากงานนี้เขียนใน pythonista จึงอาจไม่ได้ผลดีเท่ากับการใช้ spacy ซึ่งเริ่มแรกตั้งในว่าจะใช้ เนื่องจากยืมคอมเพื่อนมาเลยต้องคืน ก็เลยเปลี่ยนมาใช้ nltk อุปสรรคอีกอย่างคือยังใช้ list/dict comprehension ได้ไม่ค่อยดีบางครั้งก็เลยได้ nested in nested พอจะเอาค่าหรือข้อมูลก็ต้อง iterate หลายรอบ 

## สรุป
พอทำเสร็จเห็นว่ามันใช้งานแบบ reproducible ได้ก็ดีใจ เพราะต้องแก้แอเร่อหลายรอบมาก สิ่งที่ได้จากการเขียนงานนี้คือในหัวจะพยายามมองประเภทว่ามันอยู่ในรูปแบบไหน แล้วจะเอาออกมายังไง อีกทั้งได้ลองใช้เครื่องมืออื่น ๆ ทำให้เห็นว่าการเขียนโปรแกรมนอกจากจะใช้ความคิดสร้างสรรค์ในการเขียน ยังใช้ความคิดสร้างสรรค์ในการออกแบบด้วย โดยเฉพาะเมื่อต้องการให้มัน interactive  สุดท้ายแล้วงานชิ้นนี้จะสำเร็จได้ก็เพราะความหมกมุ่นในงานชิ้นนี้เป็นเวลาหลายวัน แต่มันจะหลายวันกว่านี้ถ้าไม่ได้ใช้เวลาในการทำ PA ต่าง ๆ ตลอดทั้งเทอม ขอบคุณอาจารย์เต้ที่ให้ความรู้ถาโถมเข้ามาแบบตู้ม 
