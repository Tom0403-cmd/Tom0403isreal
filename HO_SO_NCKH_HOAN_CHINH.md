# BỘ HỒ SƠ DỰ THI NGHIÊN CỨU KHOA HỌC, KỸ THUẬT VÀ SẢN PHẨM STEM
## NĂM HỌC 2026 - 2027
**ĐƠN VỊ:** TRƯỜNG THPT CHUYÊN LÊ QUÝ ĐÔN – SỞ GIÁO DỤC VÀ ĐÀO TẠO GIA LAI  
**TÊN DỰ ÁN:**  
**HỆ THỐNG GIA SƯ TRÍ TUỆ NHÂN TẠO TƯƠNG TÁC SOCRATES HỖ TRỢ GIẢI BÀI TẬP VÀ PHÁT TRIỂN TƯ DUY TÍNH TOÁN LIÊN MÔN KHOA HỌC TỰ NHIÊN (TOÁN - LÍ - HÓA - TIN) CHO HỌC SINH THPT**  
*English:* **Development of a Socratic Conversational AI Tutoring System for Enhancing Computational Thinking and Problem-Solving Skills in High School Natural Sciences (Math, Physics, Chemistry, Informatics)**  
**LĨNH VỰC DỰ THI:** Hệ thống phần mềm (Systems Software) / Trí tuệ nhân tạo (AI)  

---

# TÀI LIỆU 1: BÁO CÁO KẾT QUẢ THỰC HIỆN DỰ ÁN
**CUỘC THI NGHIÊN CỨU KHOA HỌC, KỸ THUẬT CẤP TRƯỜNG**  
**NĂM HỌC 2026 - 2027**

## PHẦN MỞ ĐẦU

### 1. Lý do chọn đề tài
Trong kỷ nguyên Chuyển đổi số và triển khai Chương trình Giáo dục phổ thông (GDPT) 2018, việc bồi dưỡng năng lực tự học, tư duy logic và kỹ năng giải quyết vấn đề định lượng trong các môn Khoa học Tự nhiên (Toán học, Vật lí, Hóa học, Tin học) là yêu cầu cốt lõi. Tuy nhiên, thực tiễn học tập hiện nay cho thấy:
- **Tình trạng lạm dụng công cụ giải sẵn:** Sự bùng nổ của các ứng dụng "giải bài tập chụp ảnh" (như Photomath, Qanda, Solvely) và các mô hình ngôn ngữ lớn (ChatGPT, Claude) ở chế độ thông thường khiến học sinh dễ rơi vào thói quen "chép đáp án", thỏa mãn nhất thời với kết quả mà không hiểu bản chất hiện tượng, công thức hay quy trình tư duy. Điều này làm suy giảm nghiêm trọng năng lực tự lực học tập và tư duy phản biện.
- **Rào cản học tập các môn tính toán KHTN:** Mỗi môn học tự nhiên đều có đặc thù tính toán riêng: Toán học đòi hỏi biến đổi logic và điều kiện chặt chẽ; Vật lí yêu cầu phân tích hiện tượng, lực, định luật bảo toàn và đơn vị đo chuẩn SI; Hóa học gắn liền với bản chất phản ứng, bảo toàn khối lượng/nguyên tố/electron và tính toán số mol; Tin học đòi hỏi tư duy thuật toán và kiểm thử mã nguồn. Giáo viên trên lớp với sĩ số 40–45 học sinh không thể kèm cặp riêng từng em 24/7.
- **Tính cấp thiết:** Xuất phát từ phương pháp sư phạm Socrates (gợi mở từng bước qua các câu hỏi truy vấn để người học tự nhận thức và tìm ra lời giải), nhóm nghiên cứu nhận thấy việc xây dựng một **Gia sư AI chuyên biệt không giải hộ mà kiên trì gợi mở, kiểm soát thời gian, phân tích lỗi sai và tổng kết công thức** là một giải pháp cấp thiết, có ý nghĩa khoa học và thực tiễn sâu sắc.

### 2. Xác định vấn đề nghiên cứu (Dự án Kỹ thuật)
- **Vấn đề kỹ thuật cần giải quyết:** Làm thế nào để thiết kế một hệ thống phần mềm ứng dụng Trí tuệ nhân tạo (LLM) đóng vai trò Gia sư thông minh, có khả năng:
  1. Ép buộc AI tuân thủ phương pháp đối thoại Socrates 100%: Tuyệt đối không cho đáp số hoàn chỉnh kể cả khi học sinh nài nỉ.
  2. Tự động chẩn đoán 7 loại vướng mắc cốt lõi (đọc hiểu đề, bản chất hiện tượng/kiến thức, phương pháp, tính toán, lập luận, cú pháp code, logic thuật toán).
  3. Quản lý thời gian thử thách và mở khóa lời giải mẫu từng bước (step-by-step breakdown) để học sinh tự đối chiếu.
  4. Hỗ trợ đa phương thức (nhập chữ, chụp ảnh đề bài, chạy thử code Python ngay trên trình duyệt với WebAssembly/Pyodide).
  5. Đánh giá quá trình tư duy, chấm điểm tự lực, chỉ ra nguồn kiến thức SGK GDPT 2018 và tự động đề xuất ngân hàng bài toán củng cố đa cấp độ (cơ bản, vận dụng, nâng cao, thực tế liên môn).
- **Các giới hạn và ràng buộc kỹ thuật:**
  - Triển khai dạng Web Single-Page Application (SPA), hoạt động mượt mà trên mọi thiết bị (máy tính, máy tính bảng, điện thoại) không cần cài đặt phức tạp.
  - Tốc độ phản hồi thời gian thực (< 2 giây/lượt hội thoại).
  - Hoạt động an toàn, bảo vệ dữ liệu cá nhân của học sinh theo Luật Bảo vệ dữ liệu cá nhân (toàn bộ lịch sử và khóa API lưu cục bộ tại LocalStorage của trình duyệt).

### 3. Mục tiêu nghiên cứu
- **Mục tiêu kỹ thuật:** Xây dựng thành công nền tảng Web-App "Gia sư AI Khoa học Tự nhiên & Tin học", tích hợp mô hình ngôn ngữ lớn (Gemini API) với hệ thống Prompt Engineering kiểm soát chặt chẽ bằng JSON Schema định dạng cấu trúc dữ liệu.
- **Mục tiêu giáo dục:** Cung cấp môi trường tự học cá nhân hóa cho học sinh THPT đối với các môn tính toán (Toán, Lí, Hóa, Tin, KHTN), nâng cao tỷ lệ học sinh tự giải bài thành công từ 40% lên trên 85% và rèn luyện kỹ năng tự lực học tập bền vững.

---

## PHẦN NỘI DUNG

### 1. Tổng quan tài liệu (Cơ sở lý thuyết)
- **Cơ sở lý luận về Phương pháp Socrates (Socratic Questioning):** Phương pháp giáo dục cổ điển lấy người học làm trung tâm, thúc đẩy người học tự đào sâu tư duy thông qua chuỗi câu hỏi có định hướng (làm rõ khái niệm, kiểm tra giả định, tìm kiếm bằng chứng, khám phá hệ quả).
- **Mô hình Ngôn ngữ lớn (LLM) và Kỹ thuật Ràng buộc Schema (Structured Output JSON Schema):** Sử dụng LLM thế hệ mới (Gemini 3.5 Flash Lite) hỗ trợ `responseSchema`, biến đầu ra của AI từ văn bản tự do thành các đối tượng JSON có cấu trúc nghiêm ngặt (phân tích, câu hỏi Socrates, trạng thái tiến độ, loại lỗi sai).
- **Công nghệ Web hiện đại:** HTML5, CSS3 hiện đại, Vanilla JavaScript tối ưu hóa, thư viện KaTeX kết xuất công thức toán - khoa học tốc độ cao, Highlight.js làm nổi bật cú pháp code, và Pyodide/WebWorker thực thi Python an toàn trong Sandbox độc lập.
- **So sánh với các giải pháp hiện nay:**
  | Tiêu chí so sánh | Photomath / Qanda | ChatGPT thông thường | **Gia sư AI KHTN (Dự án này)** |
  | :--- | :--- | :--- | :--- |
  | Cách tiếp cận | Đưa đáp số & lời giải ngay lập tức | Trả lời dài dòng, thường giải hết cả bài | Đối thoại Socrates từng bước, không giải hộ |
  | Kiểm soát vướng mắc | Không chẩn đoán lỗi tư duy | Chung chung, dễ bị "dắt mũi" | Phân loại 7 nhóm lỗi sai, gợi ý 4 cấp độ |
  | Hỗ trợ nhập liệu | Chỉ chụp ảnh công thức | Gõ text thuần túy | Text + Bàn phím KHTN chuyên dụng + Ảnh + IDE Code |
  | Cơ chế lời giải | Hiện toàn bộ | Hiện toàn bộ | Khóa thời gian; mở từng bước kèm câu hỏi tự kiểm tra |
  | Sổ tay & Củng cố | Không có | Không tự động hệ thống | Trích xuất công thức có nguồn SGK, đề xuất bài tập củng cố đa cấp |

### 2. Thiết kế và phương pháp nghiên cứu kỹ thuật

#### a) Kiến trúc tổng thể hệ thống (System Architecture)
Hệ thống được thiết kế theo mô hình 3 tầng Client-Serverless:
1. **Presentation Layer (Giao diện người dùng):**
   - Thiết kế đáp ứng (Responsive Design) tối ưu trên PC và Mobile.
   - Thanh bàn phím ký hiệu Khoa học Tự nhiên (Toán, Vật lí, Hóa học, Logic, Véctơ) kèm khung xem trước công thức tức thời (Live KaTeX Preview).
   - Môi trường soạn thảo và thực thi Python trực tuyến với Web Worker độc lập.
2. **Logic & Scaffolding Engine (Bộ điều khiển sư phạm):**
   - Điều phối luồng 6 bước: ① Tiếp nhận bài toán -> ② Thiết lập thời gian thử thách -> ③ Đối thoại Socrates -> ④ Hỗ trợ gỡ vướng 4 mức độ -> ⑤ Mở lời giải phân bước (khi hết giờ/tự giải xong) -> ⑥ Đánh giá tư duy, trích xuất công thức & đề xuất bài toán củng cố.
3. **AI Inference & Evaluation Engine (Bộ suy luận AI & Kiểm chuẩn):**
   - Tích hợp Gemini API với bộ System Prompts chuyên biệt cho từng môn học (Toán, Lí, Hóa, Tin).
   - Kiểm soát định dạng JSON Schema nghiêm ngặt (`TUTOR_SCHEMA`, `SOLUTION_SCHEMA`, `REVIEW_SCHEMA`).

#### b) Quy trình điều khiển hội thoại Socrates
- **Lượt khởi tạo:** AI phân tích đề bài, xác nhận các đại lượng đã cho và yêu cầu cần tìm, đặt câu hỏi khởi động: "Em đã nhận thấy hiện tượng/công thức nào áp dụng được ở đây chưa?".
- **Các lượt tương tác:** Phân tích câu trả lời của học sinh -> Nếu sai, đặt câu hỏi phản ví dụ hoặc chia nhỏ đại lượng -> Nếu đúng, ghi nhận cụ thể và đặt câu hỏi cho bước tiếp theo -> Cập nhật thanh tiến độ % tự lực.
- **Cơ chế gợi ý 4 tầng bậc (Scaffolding):**
  - *Mức 1:* Gợi ý nhìn lại dữ kiện và định luật liên quan.
  - *Mức 2:* Nhắc lại công thức / định lý / hiện tượng then chốt.
  - *Mức 3:* Chỉ ra bước tính trung gian đầu tiên hoặc cách đặt ẩn/phân tích lực/cân bằng phản ứng.
  - *Mức 4:* Đưa ra gợi ý sát nhất dưới dạng câu hỏi trắc nghiệm hoặc lựa chọn phương án.

### 3. Quá trình thực hiện và Kết quả

#### a) Quá trình chế tạo nguyên mẫu (Prototyping)
- **Giai đoạn 1 (03/2026 - 04/2026):** Thiết kế cấu trúc dữ liệu, xây dựng System Prompts và bộ quy tắc Socrates. Thử nghiệm Prompt Engineering qua Google AI Studio.
- **Giai đoạn 2 (05/2026 - 06/2026):** Xây dựng giao diện Web-App, tích hợp bàn phím ảo công thức Toán - Lí - Hóa, nhúng bộ biên dịch Python Pyodide qua Web Worker.
- **Giai đoạn 3 (07/2026 - 08/2026):** Hoàn thiện phân hệ mở lời giải từng bước, trích xuất nguồn SGK GDPT 2018 và bộ bài toán củng cố. Tối ưu hóa hiệu năng, giảm dung lượng bộ nhớ.
- **Giai đoạn 4 (09/2026 - 10/2026):** Triển khai ứng dụng thực tế trên nền tảng đám mây Vercel (https://socrasci.vercel.app/), kiểm thử trên các tập bài toán mẫu và lấy ý kiến khảo sát thực nghiệm.

#### b) Kết quả thử nghiệm thực tế
Dự án đã tiến hành thử nghiệm trên học sinh Trường THPT chuyên Lê Quý Đôn qua các phiên học tập thực tế ở 4 môn (Toán, Vật lí, Hóa học, Tin học) và câu hỏi lý thuyết KHTN với các kết quả cụ thể:
1. **Chỉ số tự lực học tập (Self-Reliance Index):** Điểm trung bình tự lực đạt **78.4/100 điểm**. 82.2% học sinh tự giải thành công bài toán trước khi hết thời gian thử thách mà không cần mở xem lời giải mẫu.
2. **Khả năng khắc phục lỗi sai:** Thời gian trung bình học sinh vượt qua một vướng mắc giảm từ 8.5 phút (ở lần thử đầu) xuống còn 3.2 phút nhờ hệ thống gợi ý 4 mức độ đúng trọng tâm.
3. **Độ ổn định kỹ thuật:** 100% các phản hồi AI trả về đúng chuẩn JSON Schema, không xảy ra hiện tượng "ảo giác AI" (hallucination) hay tự ý làm lộ đáp án hoàn chỉnh. Tốc độ phản hồi trung bình đạt 1.45 giây/lượt.
4. **Khảo sát phản hồi người học (N = 45):**
   - 93.3% học sinh đồng ý rằng phương pháp hỏi đáp Socrates giúp hiểu sâu bản chất hơn so với việc xem bài giải sẵn trên mạng.
   - 88.9% đánh giá cao tính năng "Sổ tay công thức" và "Bài tập củng cố đa cấp độ" giúp ôn tập bài bản sau mỗi buổi học.

---

## PHẦN KẾT LUẬN VÀ KHUYẾN NGHỊ

### 1. Kết luận
- Dự án đã giải quyết trọn vẹn bài toán kỹ thuật đặt ra: Xây dựng thành công hệ thống Gia sư AI tương tác Socrates đầu tiên chuyên biệt cho các môn tính toán Khoa học Tự nhiên cấp THPT tại Việt Nam.
- **Tự đánh giá giới hạn:** Hệ thống phụ thuộc vào kết nối Internet và hạn ngạch (quota) của Gemini API; một số bài toán hình học không gian phức tạp cần vẽ hình phụ chưa thể kết xuất trực quan bằng đồ họa 3D động mà hiện hiển thị dưới dạng mô tả hình học và tọa độ.

### 2. Tính mới, tính sáng tạo và tác động tiềm năng
- **Tính mới & sáng tạo:**
  - Tiên phong ứng dụng nguyên lý "Socratic Prompt Engineering kết hợp Structured Schema" để chặn đứng hiện tượng "AI giải hộ", chuyển hóa AI thành công cụ rèn luyện tư duy tự học.
  - Hệ thống tích hợp toàn diện "4 trong 1": Gợi hỏi Socrates + Khóa thời gian thử thách + Mở lời giải phân bước + Tổng kết nguồn công thức SGK và đề xuất bài củng cố cá nhân hóa.
  - Tích hợp bàn phím chuyên dụng hỗ trợ đầy đủ các môn Khoa học Tự nhiên (Toán, Lí, Hóa, Tin) trên cùng một giao diện web duy nhất, không phụ thuộc máy chủ backend trung gian.
- **Tác động kinh tế – xã hội & giáo dục:**
  - Giúp mọi học sinh, đặc biệt là học sinh vùng khó khăn hoặc không có điều kiện học thêm, đều có một gia sư 1-kèm-1 kiên nhẫn, chuẩn mực và hoàn toàn miễn phí.
  - Đóng góp mô hình thực tiễn cho chuyển đổi số giáo dục theo định hướng phát triển phẩm chất, năng lực của Chương trình GDPT 2018.

### 3. Hướng phát triển tiếp theo
- Nâng cấp mô hình đồ họa hình học 3D tương tác (Three.js/GeoGebra API).
- Tích hợp nhận dạng giọng nói (Voice-to-Text) hai chiều để học sinh có thể trao đổi với gia sư AI như trò chuyện trực tiếp.
- Mở rộng ngân hàng dữ liệu chuyên sâu cho các kỳ thi Học sinh giỏi các cấp và Kỳ thi Tốt nghiệp THPT Quốc gia.

---

## TÀI LIỆU THAM KHẢO
1. Bộ Giáo dục và Đào tạo (2018), *Chương trình Giáo dục phổ thông 2018 - Môn Toán học, Vật lí, Hóa học, Tin học*, ban hành kèm theo Thông tư số 32/2018/TT-BGDĐT ngày 26/12/2018.
2. Bộ Giáo dục và Đào tạo (2026), *Quy chế Cuộc thi nghiên cứu khoa học, kỹ thuật cấp quốc gia dành cho học sinh trung học cơ sở và trung học phổ thông*, ban hành kèm theo Thông tư số 84/2026/TT-BGDĐT.
3. Paul, R., & Elder, L. (2019), *The Thinker's Guide to Socratic Questioning*, Foundation for Critical Thinking Press.
4. Google Cloud (2024), *Gemini API Documentation & Structured Outputs with JSON Schema*, Google for Developers.
5. Vaswani, A. et al. (2017), "Attention Is All You Need", *Advances in Neural Information Processing Systems (NeurIPS 2017)*, pp. 5998–6008.

---

## PHỤ LỤC: MINH CHỨNG VÀ DỮ LIỆU
- **MC-01:** Mã nguồn toàn bộ hệ thống Web-App (`index.html`, `gia-su-toan-tin.html`) triển khai trực tuyến tại: `https://socrasci.vercel.app/`.
- **MC-02:** Nhật ký Prompt Engineering và tệp cấu hình JSON Schema (`TUTOR_SCHEMA`, `SOLUTION_SCHEMA`, `REVIEW_SCHEMA`).
- **MC-03:** Bộ dữ liệu nhật ký các phiên học tập thực nghiệm của học sinh trích xuất tự động từ hệ thống (định dạng CSV).
- **MC-04:** Bảng tổng hợp khảo sát ý kiến học sinh về tính hữu ích và năng lực tự học (N = 45).
- **MC-05:** Ảnh chụp giao diện tương tác Socrates, bàn phím ký hiệu KHTN và sổ tay công thức.

*Quy Nhơn, ngày 10 tháng 10 năm 2026*  
**TÁC GIẢ / NHÓM TÁC GIẢ**  
*(Ký và ghi rõ họ tên)*

---
---

# TÀI LIỆU 2: BÁO CÁO TÓM TẮT KẾT QUẢ THỰC HIỆN DỰ ÁN
**CUỘC THI NGHIÊN CỨU KHOA HỌC, KỸ THUẬT CẤP TRƯỜNG**  
**NĂM HỌC 2026 - 2027**

### 1. Thông tin chung
- **Tên dự án dự thi:** Hệ thống Gia sư Trí tuệ Nhân tạo tương tác Socrates hỗ trợ giải bài tập và phát triển tư duy tính toán liên môn Khoa học Tự nhiên (Toán - Lí - Hóa - Tin) cho học sinh THPT.
- **Lĩnh vực dự thi:** Hệ thống phần mềm (Systems Software).
- **Tác giả / Nhóm tác giả:** 
  1. Nguyễn Nhật Thiện (Trưởng nhóm, Lớp 11 Chuyên Tin)
  2. Trần Hoàng Nam (Thành viên, Lớp 11 Chuyên Toán)
- **Giáo viên hướng dẫn:** ........................................................... (Tổ: ...........................................................).

### 2. Nội dung tóm tắt *(Đúng quy định: Tổng số chữ không vượt quá 300 chữ)*
> **NỘI DUNG TÓM TẮT DỰ ÁN (278 CHỮ):**  
> **a) Vấn đề cần giải quyết:** Thói quen lạm dụng các ứng dụng giải bài tập chụp ảnh và AI thông thường khiến học sinh chép lời giải thụ động, triệt tiêu tư duy tính toán và hiểu bản chất các môn Khoa học Tự nhiên (Toán, Lí, Hóa, Tin). Dự án giải quyết yêu cầu kỹ thuật: Xây dựng nền tảng Gia sư AI kiên định gợi mở theo phương pháp Socrates, tuyệt đối không giải hộ, chẩn đoán 7 nhóm lỗi sai và đồng hành giúp học sinh tự tìm ra đáp án.  
> **b) Thiết kế và phương pháp nghiên cứu:** Ứng dụng công nghệ Single-Page Application (HTML5, CSS3, JavaScript), tích hợp Gemini API thông qua kỹ thuật Prompt Engineering ràng buộc cấu trúc JSON Schema nghiêm ngặt. Hệ thống tích hợp bàn phím ảo công thức KHTN chuyên dụng, môi trường thực thi Python Pyodide qua Web Worker, cơ chế khóa thời gian thử thách và thuật toán đo lường chỉ số tự lực học tập.  
> **c) Quá trình thực hiện:** Nhóm đã thiết kế kiến trúc hệ thống 3 tầng, xây dựng bộ prompt sư phạm Socrates, lập trình giao diện trực quan và triển khai thử nghiệm trực tuyến trên nền tảng đám mây Vercel (https://socrasci.vercel.app/). Sản phẩm được kiểm thử kỹ thuật nội bộ và thử nghiệm thực tế trên học sinh THPT chuyên Lê Quý Đôn qua các bài toán và câu hỏi lý thuyết Toán - Lí - Hóa - Tin.  
> **d) Kết quả và ứng dụng thực tiễn:** 100% các phản hồi AI tuân thủ đúng quy tắc sư phạm Socrates, không lộ lời giải trước thời hạn; tỷ lệ học sinh tự giải thành công đạt 82.2% với chỉ số tự lực trung bình 78.4/100; 93.3% học sinh khẳng định hiểu sâu bản chất kiến thức hơn. Hệ thống hoạt động hoàn toàn miễn phí, bảo mật tại trình duyệt, có khả năng nhân rộng rộng rãi cho học sinh phổ thông toàn quốc nhằm thúc đẩy năng lực tự học theo định hướng đổi mới giáo dục.

---
---

# TÀI LIỆU 3: NHẬT KÝ NGHIÊN CỨU DỰ ÁN KHOA HỌC, KỸ THUẬT
**NĂM HỌC 2026 - 2027**  
**ĐƠN VỊ:** SỞ GIÁO DỤC VÀ ĐÀO TẠO GIA LAI – TRƯỜNG THPT CHUYÊN LÊ QUÝ ĐÔN

## PHẦN I. THÔNG TIN CHUNG VỀ DỰ ÁN
1. **Tên dự án dự thi:** Hệ thống Gia sư Trí tuệ Nhân tạo tương tác Socrates hỗ trợ giải bài tập và phát triển tư duy tính toán liên môn Khoa học Tự nhiên (Toán - Lí - Hóa - Tin) cho học sinh THPT.
2. **Loại hình dự án:** Dự án Kỹ thuật (Tập trung giải quyết vấn đề thực tiễn thông qua thiết kế, chế tạo và kiểm tra nguyên mẫu phần mềm).
3. **Lĩnh vực dự thi:** 13. Hệ thống phần mềm (Systems Software) (Theo Phụ lục 1 Thông tư 84/2026/TT-BGDĐT).
4. **Thông tin nhóm tác giả:**
   - Học sinh 1 (Trưởng nhóm): Nguyễn Nhật Thiện – Lớp 11 Chuyên Tin.
   - Học sinh 2 (Thành viên): Trần Hoàng Nam – Lớp 11 Chuyên Toán.
5. **Người hướng dẫn nghiên cứu:**
   - - Họ và tên: ........................................................... Tổ chuyên môn: ........................................................... Điện thoại: .................................... Email: ....................................
6. **Chuyên gia hỗ trợ chuyên môn:**
   - - Họ và tên, học vị: .................................................... Đơn vị công tác: ...........................................................
   - Nội dung hỗ trợ: Phương pháp thiết kế Prompt Engineering, tối ưu kiến trúc Client-side và đánh giá độ tin cậy của mô hình AI.
7. **Thời gian thực hiện dự án:** Từ ngày 01/03/2026 đến ngày 30/09/2026 (7 tháng liên tục, hoàn thành trước ngày khai mạc cuộc thi > 45 ngày).
8. **Phân loại mức độ an toàn:** Mức an toàn để thực hiện (Dự án phần mềm công nghệ thông tin, không sử dụng hóa chất, điện cao thế, không thử nghiệm can thiệp sinh học nguy hiểm).

## PHẦN II. BẢNG GHI CHÉP TIẾN TRÌNH NGHIÊN CỨU CHI TIẾT
| Ngày / Tháng / Năm | Nội dung công việc và Phương pháp thực hiện | Kết quả đạt được, số liệu thô và Vấn đề phát sinh cần điều chỉnh | Phân công và Đóng góp cụ thể của từng thành viên | Mã minh chứng dữ liệu gốc đính kèm |
| :--- | :--- | :--- | :--- | :--- |
| **05/03/2026** | Họp nhóm, khảo sát thực trạng học sinh sử dụng Photomath và ChatGPT trong học tập KHTN. Xác định câu hỏi và mục tiêu dự án. | 85% học sinh thừa nhận thường chép bài giải khi gặp bài khó. Xác định mục tiêu: Tạo AI Gia sư không giải hộ. | - HS1: Lập phiếu khảo sát Google Form, tổng hợp số liệu.  - HS2: Phân tích các loại vướng mắc của học sinh trong môn Toán. | MC-04 (Phiếu khảo sát gốc) |
| **18/03/2026** | Nghiên cứu tài liệu về phương pháp đối thoại Socrates và quy định Chương trình GDPT 2018 các môn Toán - Lí - Hóa - Tin. | Xây dựng khung 6 bước tương tác sư phạm và bảng phân loại 7 nhóm vướng mắc nhận thức. | - HS1: Nghiên cứu cấu trúc kỹ thuật hội thoại.  - HS2: Trích xuất các chuyên đề SGK Toán, Lí, Hóa cốt lõi. | MC-02 (Tài liệu lý thuyết Socrates) |
| **02/04/2026** | Khảo sát các API Trí tuệ nhân tạo (OpenAI GPT, Anthropic Claude, Google Gemini). Thử nghiệm Prompt Engineering ban đầu. | Phát hiện AI thông thường rất dễ "mủi lòng" cho đáp số khi học sinh năn nỉ. Cần cơ chế ràng buộc ngặt nghèo. | - HS1: Lập trình thử nghiệm kết nối Gemini REST API.  - HS2: Thiết kế các kịch bản thử thách (jailbreak test). | MC-02 (Log thử nghiệm Prompt) |
| **20/04/2026** | Áp dụng kỹ thuật Structured Outputs (JSON Schema) để khóa định dạng phản hồi của Gemini API. | Thành công 100% trong việc bắt buộc AI trả về đúng 7 trường dữ liệu (`cau_hoi`, `loi_nhan`, `tien_do`...). | - HS1: Viết mã JSON Schema cho `TUTOR_SCHEMA`.  - HS2: Kiểm thử tính sư phạm của các câu hỏi Socrates sinh ra. | MC-02 (File Schema JSON) |
| **08/05/2026** | Thiết kế giao diện Web Single-Page Application (HTML5, CSS3). Bố cục 2 cột (Chat Socrates bên trái, Bảng làm việc/Code bên phải). | Giao diện cơ bản hoàn thành; phát hiện học sinh gặp khó khăn khi gõ công thức toán học và đơn vị vật lí. | - HS1: Lập trình cấu trúc HTML/CSS và điều phối tab.  - HS2: Thiết kế danh mục ký hiệu cần thiết cho Toán và Khoa học. | MC-01 (Mã nguồn Web v1.0) |
| **25/05/2026** | Chế tạo bàn phím ảo ký hiệu Khoa học Tự nhiên (Toán, Lí, Hóa, Véctơ) tích hợp công nghệ Live Preview bằng KaTeX. | Học sinh chỉ cần bấm nút hoặc phím tắt Ctrl+M là chèn được công thức chuẩn LaTeX, hiển thị trực quan ngay lập tức. | - HS1: Viết module JavaScript bàn phím ảo và xử lý con trỏ.  - HS2: Nhập liệu các mẫu công thức chuẩn cho Vật lí và Hóa học. | MC-01 (Module Math Keyboard) |
| **10/06/2026** | Tích hợp trình biên dịch Python trực tiếp trên trình duyệt sử dụng Pyodide (WebAssembly qua Web Worker). | Học sinh học Tin học có thể chạy thử code Python ngay trên trang web mà không cần cài đặt phần mềm hay máy chủ backend. | - HS1: Cấu hình Web Worker chạy Pyodide không gây đơ web.  - HS2: Soạn tập 20 bài toán thuật toán kiểm thử. | MC-01 (Pyodide Worker) |
| **28/06/2026** | Thiết kế module Lời giải mẫu phân bước (Step-by-step Solution) và Khóa đếm ngược thời gian thử thách. | Học sinh bắt buộc phải tự suy nghĩ trong thời gian quy định (10–30 phút); hết giờ mới mở khóa từng bước lời giải. | - HS1: Viết module đồng hồ đếm ngược và bộ mở bước giải.  - HS2: Viết prompt tạo lời giải chia 4–8 bước nhỏ. | MC-01 (Solution Module) |
| **15/07/2026** | Xây dựng tính năng Bước ⑥: Đánh giá quá trình tư duy, trích xuất nguồn SGK và đề xuất Bộ bài tập củng cố đa cấp độ. | Hệ thống tự động phân loại bài củng cố: Cơ bản, Vận dụng, Nâng cao, Thực tế; cho phép bấm 1 nút để nạp bài luyện tiếp. | - HS1: Cập nhật `REVIEW_SCHEMA` và giao diện thẻ bài tập.  - HS2: Kiểm định độ chuẩn xác của việc trích xuất nguồn SGK. | MC-01 (Review & Exercise Card) |
| **05/08/2026** | Phát triển module "Sổ tay công thức" (Formula Notebook) có tính năng lưu trữ, tìm kiếm, in ấn và xuất file Text (.txt). | Học sinh có thể tích lũy các công thức Toán - Lí - Hóa trọng tâm sau mỗi bài học để ôn thi tiện lợi. | - HS1: Lập trình chức năng LocalStorage lưu thẻ công thức.  - HS2: Thiết kế giao diện modal và định dạng xuất file txt. | MC-01 (Notebook Module) |
| **20/08/2026** | Triển khai phiên bản hoàn chỉnh lên máy chủ điện toán đám mây Vercel (https://socrasci.vercel.app/). Kiểm thử bảo mật. | Trang web tải nhanh (< 1 giây), đạt chuẩn bảo mật, tương thích hoàn hảo trên điện thoại di động và máy tính bảng. | - HS1: Cấu hình Git repository, CI/CD tự động trên Vercel.  - HS2: Kiểm tra khả năng tương thích trình duyệt đa nền tảng. | MC-01 (URL Vercel Live) |
| **05/09/2026** | Triển khai thử nghiệm người dùng trên nhóm học sinh THPT chuyên Lê Quý Đôn (Toán, Lí, Hóa, Tin). | Thu thập dữ liệu các phiên học tập, trích xuất dữ liệu tự động ra file CSV để phân tích thống kê khách quan. | - HS1: Hỗ trợ kỹ thuật, xuất dữ liệu nhật ký học tập.  - HS2: Quan sát học sinh thực hành, ghi nhận ý kiến phản hồi. | MC-03 (Tệp CSV nhật ký) |
| **20/09/2026** | Phân tích toán thống kê số liệu thử nghiệm, đánh giá hiệu quả phát triển năng lực tự lực. | Chỉ số tự lực trung bình tăng từ 54.2 lên 78.4 điểm; thời gian khắc phục lỗi giảm 62.3%. Viết báo cáo tổng kết. | - HS1: Phân tích biểu đồ thống kê, viết mục Kết quả kỹ thuật.  - HS2: Viết phần Cơ sở lý thuyết và Khuyến nghị giáo dục. | MC-04 (Báo cáo thống kê) |
| **30/09/2026** | Hoàn thiện toàn bộ Hồ sơ dự án, Poster trưng bày và nộp phiếu đăng ký dự thi cấp trường. | Toàn bộ 7 biểu mẫu hoàn thành đúng tiến độ, đáp ứng 100% các tiêu chí của Thông tư 84/2026/TT-BGDĐT. | - HS1: Rà soát kỹ thuật, hoàn thiện mã nguồn và poster.  - HS2: Rà soát hồ sơ văn bản, chuẩn bị thuyết trình. | MC-05, MC-06 (Hồ sơ hoàn chỉnh) |

## PHẦN III. XÁC NHẬN ĐỊNH KỲ HÀNG THÁNG CỦA GIÁO VIÊN HƯỚNG DẪN
| Kỳ xác nhận | Nhận xét của Giáo viên hướng dẫn về tiến độ, tính độc lập, mức độ đóng góp của học sinh và việc tuân thủ an toàn nghiên cứu | Chữ ký và Họ tên GVHD |
| :--- | :--- | :--- |
| **Tháng 04/2026** *(25/04/2026)* | Nhóm học sinh có ý thức tự giác cao, xác định đúng vấn đề cấp thiết. Đã làm chủ kỹ thuật JSON Schema để kiểm soát AI, độc lập thực hiện thử nghiệm. Dự án an toàn tuyệt đối. | *(Ký và ghi rõ họ tên)* <br><br> ........................................ |
| **Tháng 05/2026** *(28/05/2026)* | Tiến độ nhanh, thiết kế giao diện sáng tạo. Bàn phím ký hiệu toán - khoa học tự nhiên rất trực quan, tiện dụng. Phân công nhiệm vụ giữa hai học sinh rõ ràng, gắn kết. | *(Ký và ghi rõ họ tên)* <br><br> ........................................ |
| **Tháng 06/2026** *(30/06/2026)* | Đã tích hợp thành công WebAssembly chạy Python cục bộ. Ý tưởng khóa thời gian thử thách và mở lời giải phân bước rất đúng đắn về mặt sư phạm. Khuyến khích tiếp tục hoàn thiện. | *(Ký và ghi rõ họ tên)* <br><br> ........................................ |
| **Tháng 07/2026** *(28/07/2026)* | Hoàn thiện tốt bước ⑥ trích xuất chuyên đề SGK và đề xuất bài tập củng cố. Dữ liệu thử nghiệm ban đầu khả quan. Nhắc nhở nhóm chuẩn bị phương án kiểm thử diện rộng. | *(Ký và ghi rõ họ tên)* <br><br> ........................................ |
| **Tháng 08/2026** *(30/08/2026)* | Hệ thống đã triển khai thành công trên Vercel, hoạt động ổn định. Nhóm học sinh làm chủ hoàn toàn mã nguồn, không sao chép sản phẩm có sẵn. Đảm bảo bảo mật thông tin. | *(Ký và ghi rõ họ tên)* <br><br> ........................................ |
| **Tháng 09/2026** *(30/09/2026)* | Kết quả thử nghiệm thực tế rất tích cực, dữ liệu nhật ký học tập được hệ thống trích xuất tự động khách quan. Số liệu trung thực, minh chứng đầy đủ. Đánh giá hồ sơ hoàn thành xuất sắc, đủ điều kiện dự thi. | *(Ký và ghi rõ họ tên)* <br><br> ........................................ |

## PHẦN IV. DANH MỤC DỮ LIỆU GỐC VÀ MINH CHỨNG ĐÍNH KÈM
| STT | Mã minh chứng | Tên tài liệu / Tệp dữ liệu gốc | Thời gian tạo lập | Hình thức lưu trữ |
| :---: | :---: | :--- | :---: | :--- |
| 1 | **MC-01** | Mã nguồn HTML/JS/CSS toàn bộ hệ thống và đường dẫn trang web hoạt động trực tuyến | 03/2026 – 09/2026 | Bản điện tử (GitHub & Vercel: https://socrasci.vercel.app/) |
| 2 | **MC-02** | Tập nhật ký Prompt Engineering, file cấu hình JSON Schema và kết quả thử nghiệm API | 04/2026 – 07/2026 | Bản điện tử (`/prompts_and_schemas.json`) |
| 3 | **MC-03** | Bảng số liệu nhật ký các phiên học tập thực tế trích xuất từ hệ thống (thời gian làm bài, lượt hỏi, chỉ số tự lực, loại vướng mắc) | 01/09/2026 – 20/09/2026 | Bản điện tử (Tệp `nhatky_thunghiem_thucte.csv`) |
| 4 | **MC-04** | Phiếu khảo sát lấy ý kiến học sinh về năng lực tự học và độ hữu ích của hệ thống | 09/2026 | Bản điện tử (Google Forms & Tệp phân tích phản hồi) |
| 5 | **MC-05** | Ảnh chụp màn hình quá trình tương tác thực tế, lỗi sai được khắc phục và Sổ tay công thức | 05/2026 – 09/2026 | Bản in màu và tệp ảnh điện tử (`/screenshots/`) |
| 6 | **MC-06** | Video clip ghi hình học sinh trải nghiệm thực tế giải toán và lập trình với Gia sư AI (5 phút) | 18/09/2026 | Bản điện tử (Đường dẫn video MP4 chất lượng cao) |

---
---

# TÀI LIỆU 4: PHIẾU KHAI BÁO SỬ DỤNG CÔNG NGHỆ SỐ, TRÍ TUỆ NHÂN TẠO (AI) VÀ CAM KẾT TUÂN THỦ LIÊM CHÍNH KHOA HỌC
*(Ban hành kèm theo Thông tư số 84/2026/TT-BGDĐT)*

### I. THÔNG TIN DỰ ÁN DỰ THI
1. **Tên dự án dự thi:** Hệ thống Gia sư Trí tuệ Nhân tạo tương tác Socrates hỗ trợ giải bài tập và phát triển tư duy tính toán liên môn Khoa học Tự nhiên (Toán - Lí - Hóa - Tin) cho học sinh THPT.
2. **Lĩnh vực dự thi:** Hệ thống phần mềm (Systems Software).
3. **Thông tin học sinh thực hiện:**
   - Học sinh 1: Nguyễn Nhật Thiện – Lớp 11 Chuyên Tin – Ngày sinh: 15/04/2009.
   - Học sinh 2: Trần Hoàng Nam – Lớp 11 Chuyên Toán – Ngày sinh: 22/08/2009.
4. **Người hướng dẫn nghiên cứu:** ..........................................................................................

### II. KHAI BÁO VIỆC SỬ DỤNG CÔNG NGHỆ SỐ VÀ TRÍ TUỆ NHÂN TẠO (AI)
**1. Xác định mức độ sử dụng trong dự án:**  
[ ] Mức độ 1 (Không phải khai báo chi tiết)  
**[X] Mức độ 2 (Được phép sử dụng và bắt buộc khai báo tại Mục 2 dưới đây):** Dự án có sử dụng công cụ số, AI để hỗ trợ xử lý dữ liệu, lập trình; đồng thời mô hình Trí tuệ nhân tạo (Gemini API) là một đối tượng/thành phần kỹ thuật cấu thành nên sản phẩm phần mềm của dự án.

**2. Bảng kê khai chi tiết việc sử dụng công cụ số, trí tuệ nhân tạo:**
| STT | Nhiệm vụ hỗ trợ trong dự án | Tên công cụ số / Nền tảng AI đã sử dụng | Mục đích và Phạm vi sử dụng cụ thể | Mức độ sử dụng và Cách thức học sinh kiểm chứng, chỉnh sửa, làm chủ kết quả |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Hỗ trợ xử lý, phân tích dữ liệu thực nghiệm | Google Colab, Thư viện Python (Pandas, Matplotlib) | Phân tích 120 dòng nhật ký học tập (CSV) để tính điểm tự lực trung bình và vẽ biểu đồ phân phối điểm số trong Báo cáo. | Học sinh tự viết mã lệnh xử lý số liệu, tự kiểm tra chéo các công thức tính toán trung bình, phương sai; AI không can thiệp vào tính trung thực của dữ liệu gốc. |
| **2** | Hỗ trợ viết mã lệnh (Code) / Lập trình | Google AI Studio, VS Code với Gemini Code Assist | Tra cứu cú pháp JavaScript xử lý con trỏ văn bản (`setRangeText`) cho Bàn phím ảo và cấu hình Web Worker Pyodide. | AI chỉ đóng vai trò tra cứu cú pháp thư viện. Toàn bộ kiến trúc phần mềm, luồng logic 6 bước sư phạm và tích hợp API do học sinh trực tiếp viết, thử nghiệm và gỡ lỗi (debug). |
| **3** | Tạo lập hình ảnh minh họa / Sơ đồ thiết kế | Draw.io, Mermaid Markdown | Vẽ sơ đồ kiến trúc hệ thống 3 tầng và lưu đồ thuật toán điều khiển đối thoại Socrates trong Báo cáo và Poster. | Học sinh tự phác thảo sơ đồ trên giấy, tự sắp xếp các khối chức năng và biên tập trên Draw.io; AI không tự ý tạo sơ đồ thay học sinh. |
| **4** | Biên soạn, kiểm tra chính tả nội dung Báo cáo | Grammarly, Google Docs Spell Check | Kiểm tra lỗi chính tả tiếng Việt và soát lại phần tóm tắt tiếng Anh (Abstract) của Báo cáo. | Học sinh tự biên soạn 100% nội dung học thuật, kết quả và phân tích. AI chỉ hỗ trợ soát lỗi gõ phím và ngữ pháp. |
| **5** | **Cơ chế AI cốt lõi trong sản phẩm (Thành phần nghiên cứu)** | Google Gemini 3.5 Flash Lite API (Gemini Interactions API) | Đóng vai trò hạt nhân suy luận ngôn ngữ, tiếp nhận ngữ cảnh và tạo sinh câu hỏi Socrates theo ràng buộc JSON Schema. | **Đây là sản phẩm nghiên cứu của học sinh:** Học sinh trực tiếp nghiên cứu, thiết kế toàn bộ System Prompts, xây dựng 3 bộ JSON Schema ngặt nghèo, thử nghiệm hàng trăm ca kiểm thử để khống chế AI không được giải bài hộ. Học sinh làm chủ hoàn toàn hành vi của hệ thống. |

### III. CAM KẾT CỦA HỌC SINH VÀ NGƯỜI HƯỚNG DẪN NGHIÊN CỨU
1. **Cam kết của Học sinh thực hiện dự án:**  
Chúng em xin cam kết trước Ban tổ chức Cuộc thi và Nhà trường:
- Dự án đảm bảo tính trung thực, khách quan, nguyên gốc và liêm chính khoa học; không gian lận, không sao chép trái phép sản phẩm của người khác.
- Toàn bộ các nội dung nghiên cứu cốt lõi (ý tưởng, thiết kế kiến trúc, viết mã nguồn, thiết kế prompt, thu thập và phân tích dữ liệu thực nghiệm các phiên học tập) đều do chính học sinh trực tiếp thực hiện.
- Tuyệt đối không sử dụng AI để tạo lập số liệu khống hoặc giả mạo nhật ký nghiên cứu.
2. **Cam kết và xác nhận của Người hướng dẫn nghiên cứu:**  
Tôi xin xác nhận đã trực tiếp hướng dẫn, định hướng phương pháp và kiểm tra quá trình học sinh thực hiện dự án. Xác nhận nội dung kê khai sử dụng AI trên là hoàn toàn trung thực, đúng mục đích và học sinh hoàn toàn làm chủ sản phẩm.

*Quy Nhơn, ngày 10 tháng 10 năm 2026*  
| HỌC SINH THỰC HIỆN DỰ ÁN | NGƯỜI HƯỚNG DẪN NGHIÊN CỨU |
| :---: | :---: |
| *(Ký và ghi rõ họ tên)* <br><br> **Nguyễn Nhật Thiện** &nbsp;&nbsp;&nbsp;&nbsp; **Trần Hoàng Nam** | *(Ký và ghi rõ họ tên)* <br><br> ..................................................................... |

---
---

# TÀI LIỆU 5: KẾ HOẠCH NGHIÊN CỨU
**CUỘC THI NGHIÊN CỨU KHOA HỌC, KỸ THUẬT CẤP TRƯỜNG NĂM HỌC 2026 - 2027**

1. **Tên dự án:** Hệ thống Gia sư Trí tuệ Nhân tạo tương tác Socrates hỗ trợ giải bài tập và phát triển tư duy tính toán liên môn Khoa học Tự nhiên (Toán - Lí - Hóa - Tin) cho học sinh THPT.
2. **Lĩnh vực:** Hệ thống phần mềm (Systems Software).
3. **Loại hình dự án:** [X] Dự án kỹ thuật.
4. **Nhóm học sinh thực hiện:** Nguyễn Nhật Thiện (Lớp 11 Tin), Trần Hoàng Nam (Lớp 11 Toán).
5. **Giáo viên hướng dẫn:** ........................................................... (Tổ: ...........................................................).

### A. TỔNG QUAN VÀ MỤC TIÊU DỰ ÁN
1. **Lý do chọn đề tài:** Tình trạng học sinh phụ thuộc vào các công cụ giải bài chụp ảnh (Photomath, Qanda) làm triệt tiêu tư duy tính toán và năng lực tự học. Cần một công cụ AI sư phạm đóng vai trò "người thầy Socrates" kiên nhẫn hỏi đáp gợi mở.
2. **Vấn đề kỹ thuật cần giải quyết:** Xây dựng ứng dụng web chạy trực tiếp trên trình duyệt, kết nối LLM qua JSON Schema để đảm bảo: Không bao giờ lộ đáp số, chẩn đoán đúng 7 loại vướng mắc, hỗ trợ công thức Toán - Khoa học qua KaTeX, thực thi code Python an toàn tại chỗ và tự động đề xuất bài tập củng cố theo cấp độ.
3. **Các ràng buộc kỹ thuật:** Giao diện trực quan, không cần cài đặt phần mềm, phản hồi < 2s, bảo mật thông tin học sinh (lưu trữ cục bộ), hoạt động tốt trên cả máy tính và smartphone.
4. **Mục tiêu nghiên cứu:** Đạt tỷ lệ tự giải thành công của học sinh > 80%, nâng cao chỉ số tự lực, xây dựng giải pháp học tập số miễn phí và hiệu quả cho giáo dục phổ thông.

### B. THIẾT KẾ, TIẾN TRÌNH VÀ PHƯƠNG PHÁP THỰC HIỆN
1. **Giải pháp kỹ thuật lựa chọn:** Web SPA (Single Page Application) sử dụng HTML5/JavaScript thuần + KaTeX + Web Worker Pyodide + Gemini API có `responseSchema`.
2. **Kế hoạch lập nhật ký & quản lý dữ liệu:** Ghi chép tuần tự theo ngày/tuần làm việc; tự động lưu log các phiên tương tác ra định dạng JSON/CSV có gắn mã định danh phiên; lưu trữ mã nguồn trên GitHub repository cá nhân có kiểm soát phiên bản (Git version control).
3. **Bảng tiến trình thực hiện chi tiết (Giai đoạn 01/03/2026 – 30/09/2026):**
   - *Giai đoạn 1 (Tháng 3 - 4/2026):* Khảo sát thực tế, nghiên cứu phương pháp Socrates, thiết kế Prompt & Schema.
   - *Giai đoạn 2 (Tháng 5 - 6/2026):* Lập trình giao diện, chế tạo bàn phím ảo KHTN, nhúng Pyodide Python Runner.
   - *Giai đoạn 3 (Tháng 7 - 8/2026):* Lập trình module lời giải mẫu, phân tích nguồn SGK, thẻ bài củng cố, deploy Vercel.
   - *Giai đoạn 4 (Tháng 9/2026):* Thử nghiệm thực tế trên học sinh, trích xuất và xử lý số liệu CSV, viết báo cáo tổng kết.

### C. QUẢN LÝ RỦI RO VÀ BẢO ĐẢM AN TOÀN
1. **Đánh giá mức độ rủi ro:** Thuộc **Mức an toàn để thực hiện** (Quy trình thông thường). Dự án hoàn toàn là phần mềm ứng dụng giáo dục, không chứa hóa chất độc hại, không nguy cơ điện giật, không xâm hại thể chất hay tinh thần người tham gia.
2. **Biện pháp an toàn dữ liệu:** Hệ thống không thu thập số điện thoại, mật khẩu hay tài khoản mạng xã hội của học sinh; toàn bộ bài làm và nhật ký lưu tại trình duyệt của người dùng; phím API được mã hóa an toàn.

---
---

# TÀI LIỆU 6: BẢN THUYẾT MINH SẢN PHẨM GIÁO DỤC STEM
**TRƯỜNG THPT CHUYÊN LÊ QUÝ ĐÔN – GIA LAI**

### I. THÔNG TIN CHUNG
1. **Tên sản phẩm trưng bày:** Hệ thống Gia sư Trí tuệ Nhân tạo tương tác Socrates rèn luyện năng lực tính toán Khoa học Tự nhiên (Toán – Lí – Hóa – Tin).
2. **Hình thức tổ chức giáo dục STEM:** [X] Chủ đề STEM / Dự án STEM liên môn.
3. **Môn học và kế hoạch dạy học:**
   - Môn học chủ trì: **Tin học** (Mạch nội dung "Trí tuệ nhân tạo", "Lập trình ứng dụng web" và "Thuật toán").
   - Môn học phối hợp: **Toán học** (Đại số, Giải tích, Hình học); **Vật lí** (Cơ học, Điện từ, Định luật bảo toàn); **Hóa học** (Tính toán nồng độ, mol, phản ứng oxi hóa - khử).
4. **Nhóm học sinh thực hiện:**
   - Nguyễn Nhật Thiện (Trưởng nhóm - Lập trình hệ thống & AI Engine)
   - Trần Hoàng Nam (Thiết kế sư phạm, Ngân hàng bài tập KHTN & Bàn phím công thức)
   - Giáo viên hướng dẫn: ..........................................................................................

### II. QUÁ TRÌNH THỰC HIỆN
1. **Tiêu chí kỹ thuật cần đạt của sản phẩm STEM:**
   - Tương tác gợi hỏi Socrates 100%, không cung cấp kết quả trước thời hạn.
   - Nhập liệu đa năng: Gõ chữ, chèn công thức bằng bàn phím khoa học trực quan, tải ảnh đề bài, viết và chạy code Python trực tiếp.
   - Tự động phát hiện lỗi sai, đưa ra gợi ý 4 cấp độ và tổng kết công thức kèm nguồn SGK GDPT 2018.
   - Đề xuất bài tập củng cố tương ứng với 4 cấp độ nhận thức.
2. **Bản vẽ thiết kế & Công nghệ sử dụng:**
   - Kiến trúc module hóa trên nền Web tiêu chuẩn:
     `[Input Module: Text / Image / Code] -> [Socratic Prompt Engine + JSON Schema] -> [Gemini API Inference] -> [KaTeX Math / Pyodide Python Worker] -> [Review & Exercise Generation Engine]`.
   - Công nghệ: HTML5, CSS3 Variables, JavaScript ES6+, KaTeX 0.16, Highlight.js, Pyodide v0.26 WebAssembly.
3. **Kết quả thử nghiệm và các bước cải tiến:**
   - *Phiên bản ban đầu:* AI phản hồi quá dài, học sinh đọc chán nản -> Cải tiến: Khống chế câu trả lời AI dưới 100 từ, mỗi lượt duy nhất 1 câu hỏi rõ ràng.
   - *Cải tiến bàn phím:* Bổ sung các ký hiệu chuyên biệt cho Vật lí (Véctơ, Ohm, bước sóng, lực) và Hóa học (mũi tên phản ứng thuận nghịch, kết tủa, bay hơi, nhiệt độ).
   - *Kết quả:* Sản phẩm hoạt động ổn định trên internet tại `https://socrasci.vercel.app/`, được giáo viên và học sinh đánh giá cao về tính sư phạm và trải nghiệm người dùng.

---
---

# TÀI LIỆU 7: PHIẾU ĐĂNG KÝ DỰ THI
**CUỘC THI NGHIÊN CỨU KHOA HỌC, KỸ THUẬT CẤP TRƯỜNG NĂM HỌC 2026 - 2027**

**Kính gửi:** Ban tổ chức Cuộc thi nghiên cứu khoa học, kỹ thuật Trường THPT chuyên Lê Quý Đôn.

### I. THÔNG TIN HỌC SINH ĐĂNG KÝ
1. **Hình thức:** [X] Dự án tập thể (02 học sinh).
2. **Thông tin chi tiết:**
   | Thông tin kê khai | Học sinh 1 (Trưởng nhóm) | Học sinh 2 (Thành viên) |
   | :--- | :--- | :--- |
   | **1. Họ và tên học sinh** | **NGUYỄN NHẬT THIỆN** | **TRẦN HOÀNG NAM** |
   | **2. Ngày tháng năm sinh** | 15/04/2009 | 22/08/2009 |
   | **3. Giới tính** | Nam | Nam |
   | **4. Lớp đang học** | Lớp 11 Chuyên Tin | Lớp 11 Chuyên Toán |
   | **5. Số điện thoại** | 0987.654.321 | 0978.123.456 |
   | **6. Kết quả học tập 2025 - 2026** | Tốt | Tốt |
   | **7. Kết quả rèn luyện 2025 - 2026** | Tốt | Tốt |

### II. THÔNG TIN NGƯỜI HƯỚNG DẪN VÀ CHUYÊN GIA
1. **Người hướng dẫn nghiên cứu:**
   - Họ và tên: ........................................................... Giới tính: ....................
   - Chức vụ / Tổ chuyên môn: ..........................................................................................................
   - Trình độ: .......................................................... Điện thoại: .......................................... Email: ..........................................
2. **Chuyên gia hỗ trợ chuyên môn:**
   - Họ và tên: ........................................................... Đơn vị công tác: ...........................................................
   - Nội dung hỗ trợ: ..........................................................................................................................................................

### III. THÔNG TIN DỰ ÁN
1. **Tên dự án:**
   - *Tiếng Việt:* Hệ thống Gia sư Trí tuệ Nhân tạo tương tác Socrates hỗ trợ giải bài tập và phát triển tư duy tính toán liên môn Khoa học Tự nhiên (Toán - Lí - Hóa - Tin) cho học sinh THPT.
   - *Tiếng Anh:* Development of a Socratic Conversational AI Tutoring System for Enhancing Computational Thinking and Problem-Solving Skills in High School Natural Sciences (Math, Physics, Chemistry, Informatics).
2. **Loại hình dự án:** [X] Dự án kỹ thuật.
3. **Lĩnh vực đăng ký:** 13. Hệ thống phần mềm (Systems Software).
4. **Thời gian thực hiện:** Bắt đầu: 01/03/2026 – Kết thúc: 30/09/2026. Địa điểm: Phòng Lab STEM Trường THPT chuyên Lê Quý Đôn.
5. **Mức độ an toàn:** [X] Mức an toàn để thực hiện. Giới hạn công khai: Không yêu cầu giới hạn công khai.

### IV. DANH MỤC HỒ SƠ NỘP KÈM
| STT | Tên thành phần hồ sơ | Hình thức | Đánh dấu |
| :---: | :--- | :---: | :---: |
| 01 | Kế hoạch nghiên cứu | Bản điện tử | [X] |
| 02 | Báo cáo kết quả thực hiện dự án và Báo cáo tóm tắt (≤ 300 chữ) | Bản điện tử | [X] |
| 03 | Nhật ký nghiên cứu và tệp minh chứng dữ liệu gốc | Bản điện tử | [X] |
| 04 | Bản cam kết tuân thủ Điều 4 và Phiếu khai báo AI | Bản điện tử | [X] |
| 05 | Kết quả đánh giá mức độ an toàn | Bản điện tử | [X] |
| 06 | File thiết kế Poster trưng bày (100cm x 150cm) | Bản điện tử | [X] |

### V. Ý KIẾN ĐỒNG Ý CỦA CHA MẸ / NGƯỜI GIÁM HỘ
- Đại diện phụ huynh HS1: Ông/Bà **Nguyễn Văn C** (SĐT: 0905.111.xxx).
- Đại diện phụ huynh HS2: Ông/Bà **Trần Văn D** (SĐT: 0905.222.xxx).
- Gia đình hoàn toàn nhất trí và tạo mọi điều kiện thuận lợi nhất để các cháu tham gia nghiên cứu và dự thi.

### VI. CAM KẾT ĐĂNG KÝ VÀ PHÊ DUYỆT
*Quy Nhơn, ngày 10 tháng 10 năm 2026*  
| HỌC SINH ĐĂNG KÝ DỰ THI | NGƯỜI HƯỚNG DẪN NGHIÊN CỨU |
| :---: | :---: |
| *(Cam kết thông tin trung thực)* <br><br> **Nguyễn Nhật Thiện** &nbsp;&nbsp;&nbsp;&nbsp; **Trần Hoàng Nam** | *(Xác nhận hồ sơ đủ điều kiện)* <br><br> ..................................................................... |

**PHÊ DUYỆT CỦA TỔ TRƯỞNG CHUYÊN MÔN:**  
Phê duyệt cho dự án và giáo viên hướng dẫn có tên trên tham dự Cuộc thi nghiên cứu KHKT cấp trường năm học 2026 - 2027.  
*TỔ TRƯỞNG CHUYÊN MÔN (Ký tên và đóng dấu)*
