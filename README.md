# 粵語繪文字

基於 [Rime 繪文字](https://github.com/rime/rime-emoji) 項目

## 自助安裝

1. 下載`opencc`檔案夾內容，將完整檔案夾放入Rime用戶檔案夾內

2. 將`emoji_suggestion.yaml`內的內容加入至想添加Emoji的方案custom檔中

## 修改內容

### `opencc/emoji_cantonese.txt`

1. 移除所有簡體詞彙，以減小檔案大小
2. 移除大部份非粵語用詞（僅保留少許台灣用詞），並補充缺少的粵語用詞（以香港粵語為主）
3. 如某繪文字可同時以多個相同字頭的詞彙輸入，在不造成歧義及不偏離原意的情況下，移除較長的詞彙（例如，保留「耳」但移除「耳朵」）
4. 對於職業類繪文字，加入性別在前的詞彙以適應自然語言（例如，保留「醫生男」並加入「男醫生」）
5. 其他修改未盡記錄

### `scripts`

新增兩個 Python 腳本以協助進行詞庫編輯

提升詞庫質素：見[CONTRIBUTING](CONTRIBUTING.md)

授權條款：見 [LICENSE](LICENSE)
