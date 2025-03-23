
### Mô tả thuật toán DES

1. **Hoán vị ban đầu (IP)**: Dữ liệu 64-bit được hoán vị theo bảng IP.  
2. **Chia dữ liệu**: Sau khi hoán vị, dữ liệu được tách thành hai nửa:  
   - **L (32-bit)**  
   - **R (32-bit)**  
3. **16 vòng Feistel**:  
   - **Mở rộng R (E-box)**: Từ 32-bit thành 48-bit.  
   - **XOR với khóa con**: Mỗi vòng sử dụng một khóa con 48-bit.  
   - **S-boxes**: Chia 48-bit thành 8 nhóm (6-bit mỗi nhóm), qua 8 bảng S-box để nén thành 32-bit.  
   - **P-box**: Hoán vị 32-bit đầu ra của S-box.  
4. **Hoán vị cuối cùng (FP)**: Sau 16 vòng, kết hợp R và L theo thứ tự đảo ngược (R + L), sau đó hoán vị theo bảng FP để tạo block mã hóa 64-bit.  
5. **Sinh khóa con (Key Schedule)**:  
   - Loại bỏ 8 bit chẵn lẻ từ khóa 64-bit, còn lại 56-bit (PC-1).  
   - Chia thành hai phần: **C (28-bit)** và **D (28-bit)**.  
   - Dịch trái và hoán vị qua PC-2 để tạo ra 16 khóa con 48-bit.  
6. **Giải mã**: Quá trình tương tự mã hóa nhưng sử dụng các khóa con theo thứ tự ngược lại (từ subkey 15 đến subkey 0).  
