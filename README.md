# SimpleTextSimilarityAPI
  - stopword.txt: danh sách các stop words sẽ được lọc ra khỏi câu khi so sánh hai câu
  - vocab.txt: danh sách các từ được chấp nhận đúng chính tả
  - validate.py: cung cấp hàm kiểm tra câu nhập vào có được chấp nhận hay không (quá ngắn, không đúng chính tả, trùng lặp)
  - api.py: tạo api ở port /api/validate và hỗ trợ method post để kiểm tra hai câu
