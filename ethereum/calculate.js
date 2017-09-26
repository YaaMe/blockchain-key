var keythereum = require("keythereum")

var params = { keyBytes: 32, ivBytes: 16 }

var keyObject = require(`./${process.env.FILE}`)
keythereum.recover(process.env.PASSWORD, keyObject, function(private_key) {
  console.log('0x'+Buffer.from(private_key).toString('hex'))
})
