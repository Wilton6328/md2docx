"""
PDF 轉換功能測試腳本
"""

from md_to_word_converter import MarkdownToPdfConverter
import os

def test_pdf_conversion():
    """測試 PDF 轉換功能"""
    print("=" * 50)
    print("Markdown to PDF Converter - 功能測試")
    print("=" * 50)
    
    # 初始化轉換器
    converter = MarkdownToPdfConverter()
    
    # 設定檔案路徑
    input_file = "test_sample.md"
    output_file = "test_output.pdf"
    
    # 檢查輸入檔案
    if not os.path.exists(input_file):
        print(f"[X] 錯誤：找不到測試檔案 {input_file}")
        return False
    
    print(f"\n輸入檔案: {input_file}")
    print(f"輸出檔案: {output_file}")
    print("\n開始轉換...")
    
    try:
        # 執行轉換
        converter.convert(input_file, output_file)
        
        # 驗證輸出
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file)
            print(f"\n[OK] 轉換成功！")
            print(f"檔案大小: {file_size:,} bytes")
            
            return True
        else:
            print(f"\n[X] 錯誤：輸出檔案未建立")
            return False
            
    except Exception as e:
        print(f"\n[X] 轉換失敗：{str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_pdf_conversion()
    print("\n" + "=" * 50)
    if success:
        print("[OK] 測試通過！")
        print("\n你現在可以：")
        print("1. 執行主程式: python md_to_word_converter.py")
        print("2. 開啟 test_output.pdf 查看轉換結果")
    else:
        print("[FAILED] 測試失敗！")
    print("=" * 50)
