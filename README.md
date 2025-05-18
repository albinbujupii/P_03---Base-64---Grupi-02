# P_03---Base-64---Grupi-2

📌 Përshkrimi i Projektit

Ky projekt ofron një implementim të thjeshtë të algoritmit Base64 për kodim dhe dekodim të tekstit, i ndërtuar në gjuhën Python.
Nuk përdor biblioteka apo klasa të gatshme si base64, dhe çdo funksionalitet është realizuar nga e para me logjikë bazë (bit manipulation, tekst dhe listat).

Programi përmban një menu interaktive, ku përdoruesi mund të zgjedhë nëse dëshiron të kodojë apo dekodojë një tekst në/fund nga Base64.

🔧 Përbërja e Kodit

Kodi është i ndarë në këto pjesë funksionale:
1.	to_binary_string(text) – Konverton tekstin në një varg bitësh 8-bit.
2.	base64_encode(text) – Kodon tekstin në Base64, duke ndarë bitët në 6-bit dhe i mappon në alfabetin e Base64.
3.	base64_decode(encoded_text) – Rikthen tekstin e koduar duke kthyer bitët në 8-bit dhe dekoduar karakteret.
4.	Menuja interaktive – Mundëson zgjedhjen nga përdoruesi për kodim ose dekodim dhe merr inputin përkatës.

🧪  Si Funksionon
	•	Kodimi: Teksti shndërrohet në binar, ndahet në 6-bit, pastaj përkthehet në karaktere të Base64. Shtohet padding = në fund nëse është e nevojshme.
	•	Dekodimi: Hiqet padding, çdo karakter Base64 konvertohet në 6-bit, dhe rikthehen karakteret origjinale nga çdo 8-bit.

🔹 Shembull përdorimi:

   Zgjidh një veprim:
   1. Enkripto në Base64
   2. Dekripto nga Base64
    Zgjedhja jote (1/2): 1
    Shkruaj tekstin që dëshiron të enkriptohet: Hello
    Teksti i enkriptuar: SGVsbG8=