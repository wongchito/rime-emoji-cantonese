# 繼續提升詞庫質素

## 基於詞彙的編輯

* 若閣下需新增或移除某詞彙所對應之繪文字，可直接對`opencc/emoji_cantonese.txt`之相應行之結尾編輯
* 請注意保持原本格式，否則部署時可能出現錯誤

## 基於繪文字的編輯

* 若閣下需新增或移除用於輸入某繪文字之詞彙，請按以下步驟進行
  1. 確保已安裝 Python 3
  2. 於終端機(Mac)或命令提示字元(Windows)執行
    ```shell
    $ cat opencc/emoji_cantonese.txt | python3 scripts/parse.py > temp/emoji_inverted.txt
    ```
  3. 按需編輯`temp/emoji_inverted.txt`，請注意保持原本格式及平衡性（如區分不同性別之繪文字之輸入詞彙）
  4. 於終端機(Mac)或命令提示字元(Windows)執行
    ```shell
    $ cat temp/emoji_inverted.txt | python3 scripts/compile.py > opencc/emoji_cantonese.txt
    ```
