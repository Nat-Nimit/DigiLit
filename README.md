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

ศึกษาการใช้ Numpy, pyplot, time, sys.stdout, การรวม list, การหาsubsetใน list, เป็นต้น


## ผลการดำเนินการ



## อุปสรรค

## สรุป
