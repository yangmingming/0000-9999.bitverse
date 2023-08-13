# 链下子集索引格式.md
[toc]



# 链下子集索引格式
修订记录：

|日期|版本号|修订说明|编制/修订人|
| ----- | ----- | ----- | ----- |
|2023-08-13|v0.1.0|初稿|vimyang|

## 格式
文件名：inscriptions.json

```Plain Text
[
  {
    "id": "",                    # inscription id
    "meta": {
      "name": ""                 # inscription name
    }
  },
  ...
]
[
  {
    "id": "",
    "meta": {
      "name": "",
      "inscription": ,
      "content_type": "",
      "content_length": ""
    },
    "tx": {
      "transaction": "",
      "timestamp": "",
      "block_id": ,
      "genesis_fee": ,
      "receive_address": ""
    }
  }
]
```


铭文id，铭文内容，铭文序号，初次mint时间，mint发起和接收地址

|字段名|字段内容|其他|
| ----- | ----- | ----- |
|id|铭文id| |
|meta| |铭文meta信息|
|meta.name|域名| |
|meta.inscription|铭文序号| |
|meta.content\_type|铭文类型|文本格式时可选|
|meta.content\_length|铭文长度|可选|
|tx| |交易相关|
|tx.transaction|铭文创建交易id| |
|tx.timestamp|铭文创建交易时间| |
|tx.block\_id|交易区块| |
|tx.genesis\_fee|交易手续费| |
|tx.receive\_address|铭文创建接收地址| |

## 举例
```Plain Text
[
  {
    "id": "855681a192ad6de8c2d26b9f52066e2e1dc88f738763acb5c775694f89dc53e4i0",
    "meta": {
      "name": "0002.bitverse",
      "inscription": 21588368,
      "content_type": "text/plain;charset=utf-8",
      "content_length": "13 bytes"
    },
    "tx": {
      "transaction": "855681a192ad6de8c2d26b9f52066e2e1dc88f738763acb5c775694f89dc53e4",
      "timestamp": "2023-08-06 01:00:02 UTC",
      "block_id": 801852,
      "genesis_fee": 1430,
      "receive_address": "bc1q3uwkd5zm7spyxfdhguwvhx74hfdy5ytrwage4s"
    }
  }
]
```
