const CryptoJS=require("./crypto");
function  getToken(player) {
      let key = CryptoJS.enc.Utf8.parse(this.key)
      const {name, birthday, height, weight} = player
      let base64Name = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(name))
      let encrypted = CryptoJS.DES.encrypt(`${base64Name}${birthday}${height}${weight}`, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
      })
      return encrypted.toString()
    }

const player = {
    name: '詹姆斯-哈登',
    image: 'harden.png',
    birthday: '1989-08-26',
    height: '196cm',
    weight: '99.8KG'
}
console.log(getToken(player))