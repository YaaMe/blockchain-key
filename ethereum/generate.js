var keythereum = require("keythereum")

var params = { keyBytes: 32, ivBytes: 16 }
var options = {
  kdf: "pbkdf2",
  cipher: "aes-128-ctr",
  kdfparams: {
    c: 212354,
    dklen: 32,
    prf: "hmac-sha256"
  }
};
var dk = keythereum.create(params)

var keyObject = keythereum.dump(process.env.PASSWORD, dk.privateKey, dk.salt, dk.iv, options);

console.log(JSON.stringify(keyObject))
