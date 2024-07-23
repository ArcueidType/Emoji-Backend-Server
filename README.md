# 表情包模板·接口文档

+ **所有 Response 格式均为：**
  + 正确响应：`'code'` : 200，`'msg'` : 'ok'，`'result'` : bytes（Image）
  + 错误响应：`'code'` : 500，`'msg'` : 'Process Procedure Error: {`error`}'

### 图片表情包

|                          表情包模板                          |       路由        |                           Request                            |
| :----------------------------------------------------------: | :---------------: | :----------------------------------------------------------: |
| <img src="./image/aceattorney.png" alt="bbd9225cdb61aae71c977668639cdb1" style="zoom: 12%;" /> |  `/aceattorney`   |                        `'text'` : str                        |
| <img src="./image/colorful.png" alt="9fa46ef2e3d05c89c87c2de37317b99" style="zoom: 15%;" /> |    `/colorful`    |        `'text1'` : str  <br />`'text2'` : str  <br />        |
| <img src="./image/bluearchive.png" alt="微信图片_20240723035316" style="zoom: 20%;" /> |   `bluearchive`   |        `'text1'` : str  <br />`'text2'` : str  <br />        |
| <img src="./image/graywordmeme.jpg" alt="589c1310a37e72bae454be9ac74b103b" style="zoom: 25%;" /> |  `/graywordmeme`  |         `'img'` : bytes<br />`'text'` : str  <br />          |
| <img src="./image/always.jpg" alt="9bf3539bfcb7a80750e2ecd5b63ba96b" style="zoom:25%;" /> |     `/always`     |                       `'img'` : bytes                        |
| <img src="./image/fightsunuo.jpg" alt="b44ce6fae5b831b8d65a8281c277250e" style="zoom: 40%;" /> |   `/fightsunuo`   |                       `'img'` : bytes                        |
| <img src="./image/luxun.png" alt="6a9e87c54edd545a0d4ccb6b9b43d03" style="zoom: 25%;" /> |     `/luxun`      |                        `'text'` : str                        |
| <img src="./image/cannot.png" alt="5cfd1b0292efbdd363d5a8226c0bd42" style="zoom: 25%;" /> |     `/cannot`     |                       `'img'` : bytes                        |
| <img src="./image/ecnublackboard.png" alt="ecnu" style="zoom:30%;" /> | `/ecnublackboard` |                        `'text'` : str                        |
| <img src="./image/ecnulion.png" alt="ecnu_lion" style="zoom:30%;" /> |    `/ecnulion`    |                        `'text'` : str                        |
| <img src="./image/trance.jpg" alt="trance" style="zoom: 20%;" /> |     `/trance`     |                       `'img'` : bytes                        |
| <img src="./image/bodysegment.png" alt="分割丁真" style="zoom: 10%;" /> |  `/bodysegment`   |                       `'img'` : bytes                        |
| <img src="./image/japanface.jpg" alt="img" style="zoom:5%;" /><img src="./image/sketchportrait.jpg" alt="img" style="zoom:5%;" /><br /><img src="./image/shinkai.jpg" alt="img" style="zoom:5%;" /><img src="./image/hayao.jpg" alt="img" style="zoom:5%;" /><br /> |    `/animegen`    | `'img'` : bytes<br />`'type'` : str {'宫崎骏', '新海诚', '日本风', '素描风'} |

---

### GIF 表情包

|                          表情包模板                          |      路由      |                    Request                    |
| :----------------------------------------------------------: | :------------: | :-------------------------------------------: |
| <img src="./image/chase_train.gif" alt="chase_train" style="zoom: 67%;" /> | `/chasetrain`  |                `'img'` : bytes                |
| <img src="./image/confuse.gif" alt="confuse" style="zoom: 33%;" /> |   `/confuse`   |                `'img'` : bytes                |
| <img src="./image/flash_blind.gif" alt="flash_blind" style="zoom: 25%;" /> | `/flashblind`  |  `'img'` : bytes<br />`'text'` : str  <br />  |
| <img src="./image/funny_mirror.gif" alt="funny_mirror" style="zoom:25%;" /> | `/funnymirror` |                `'img'` : bytes                |
| <img src="./image/guichu.gif" alt="guichu" style="zoom:20%;" /> |   `/guichu`    |  `'img'` : bytes<br />`'text'` : str  <br />  |
| <img src="./image/kiss.gif" alt="kiss" style="zoom: 67%;" /> |    `/kiss`     | `'img1'` : bytes<br />`'img2'` : bytes<br />  |
|  <img src="./image/rub.gif" alt="rub" style="zoom: 50%;" />  |     `/rub`     | `'img1'` : bytes<br /> `'img2'` : bytes<br /> |
| <img src="./image/punch.gif" alt="punch" style="zoom:37%;" /> |    `/punch`    |                `'img'` : bytes                |
| <img src="./image/play.gif" alt="play" style="zoom:33%;" />  |     `play`     |                `'img'` : bytes                |

