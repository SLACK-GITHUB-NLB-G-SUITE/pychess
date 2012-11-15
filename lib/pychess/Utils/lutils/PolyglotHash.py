# -*- coding: UTF-8 -*-

# Polyglot opening books are indexed by 64-bit Zobrist hash keys.
# The standard specifies the following Zobrist seed values.
# The numbers in this file come from PolyGlot by Fabien Letouzey.
# PolyGlot is available under the GNU GPL from http://wbec-ridderkerk.nl

pieceHashes = [
  [
    [ 0x0000000000000000 ] * 64,
    [ 0x5355f900c2a82dc7, 0x07fb9f855a997142, 0x5093417aa8a7ed5e, 0x7bcbc38da25a7f3c, 
      0x19fc8a768cf4b6d4, 0x637a7780decfc0d9, 0x8249a47aee0e41f7, 0x79ad695501e7d1e8, 
      0x14acbaf4777d5776, 0xf145b6beccdea195, 0xdabf2ac8201752fc, 0x24c3c94df9c8d3f6, 
      0xbb6e2924f03912ea, 0x0ce26c0b95c980d9, 0xa49cd132bfbf7cc4, 0xe99d662af4243939, 
      0x27e6ad7891165c3f, 0x8535f040b9744ff1, 0x54b3f4fa5f40d873, 0x72b12c32127fed2b, 
      0xee954d3c7b411f47, 0x9a85ac909a24eaa1, 0x70ac4cd9f04f21f5, 0xf9b89d3e99a075c2, 
      0x87b3e2b2b5c907b1, 0xa366e5b8c54f48b8, 0xae4a9346cc3f7cf2, 0x1920c04d47267bbd, 
      0x87bf02c6b49e2ae9, 0x092237ac237f3859, 0xff07f64ef8ed14d0, 0x8de8dca9f03cc54e, 
      0x9c1633264db49c89, 0xb3f22c3d0b0b38ed, 0x390e5fb44d01144b, 0x5bfea5b4712768e9, 
      0x1e1032911fa78984, 0x9a74acb964e78cb3, 0x4f80f7a035dafb04, 0x6304d09a0b3738c4, 
      0x2171e64683023a08, 0x5b9b63eb9ceff80c, 0x506aacf489889342, 0x1881afc9a3a701d6, 
      0x6503080440750644, 0xdfd395339cdbf4a7, 0xef927dbcf00c20f2, 0x7b32f7d1e03680ec, 
      0xb9fd7620e7316243, 0x05a7e8a57db91b77, 0xb5889c6e15630a75, 0x4a750a09ce9573f7, 
      0xcf464cec899a2f8a, 0xf538639ce705b824, 0x3c79a0ff5580ef7f, 0xede6c87f8477609d, 
      0x799e81f05bc93f31, 0x86536b8cf3428a8c, 0x97d7374c60087b73, 0xa246637cff328532, 
      0x043fcae60cc0eba0, 0x920e449535dd359e, 0x70eb093b15b290cc, 0x73a1921916591cbd, 
    ],
    [ 0xc547f57e42a7444e, 0x78e37644e7cad29e, 0xfe9a44e9362f05fa, 0x08bd35cc38336615, 
      0x9315e5eb3a129ace, 0x94061b871e04df75, 0xdf1d9f9d784ba010, 0x3bba57b68871b59d, 
      0xd2b7adeeded1f73f, 0xf7a255d83bc373f8, 0xd7f4f2448c0ceb81, 0xd95be88cd210ffa7, 
      0x336f52f8ff4728e7, 0xa74049dac312ac71, 0xa2f61bb6e437fdb5, 0x4f2a5cb07f6a35b3, 
      0x87d380bda5bf7859, 0x16b9f7e06c453a21, 0x7ba2484c8a0fd54e, 0xf3a678cad9a2e38c, 
      0x39b0bf7dde437ba2, 0xfcaf55c1bf8a4424, 0x18fcf680573fa594, 0x4c0563b89f495ac3, 
      0x40e087931a00930d, 0x8cffa9412eb642c1, 0x68ca39053261169f, 0x7a1ee967d27579e2, 
      0x9d1d60e5076f5b6f, 0x3810e399b6f65ba2, 0x32095b6d4ab5f9b1, 0x35cab62109dd038a, 
      0xa90b24499fcfafb1, 0x77a225a07cc2c6bd, 0x513e5e634c70e331, 0x4361c0ca3f692f12, 
      0xd941aca44b20a45b, 0x528f7c8602c5807b, 0x52ab92beb9613989, 0x9d1dfa2efc557f73, 
      0x722ff175f572c348, 0x1d1260a51107fe97, 0x7a249a57ec0c9ba2, 0x04208fe9e8f7f2d6, 
      0x5a110c6058b920a0, 0x0cd9a497658a5698, 0x56fd23c8f9715a4c, 0x284c847b9d887aae, 
      0x04feabfbbdb619cb, 0x742e1e651c60ba83, 0x9a9632e65904ad3c, 0x881b82a13b51b9e2, 
      0x506e6744cd974924, 0xb0183db56ffc6a79, 0x0ed9b915c66ed37e, 0x5e11e86d5873d484, 
      0xf678647e3519ac6e, 0x1b85d488d0f20cc5, 0xdab9fe6525d89021, 0x0d151d86adb73615, 
      0xa865a54edcc0f019, 0x93c42566aef98ffb, 0x99e7afeabe000731, 0x48cbff086ddf285a, 
    ],
    [ 0x23b70edb1955c4bf, 0xc330de426430f69d, 0x4715ed43e8a45c0a, 0xa8d7e4dab780a08d, 
      0x0572b974f03ce0bb, 0xb57d2e985e1419c7, 0xe8d9ecbe2cf3d73f, 0x2fe4b17170e59750, 
      0x11317ba87905e790, 0x7fbf21ec8a1f45ec, 0x1725cabfcb045b00, 0x964e915cd5e2b207, 
      0x3e2b8bcbf016d66d, 0xbe7444e39328a0ac, 0xf85b2b4fbcde44b7, 0x49353fea39ba63b1, 
      0x1dd01aafcd53486a, 0x1fca8a92fd719f85, 0xfc7c95d827357afa, 0x18a6a990c8b35ebd, 
      0xcccb7005c6b9c28d, 0x3bdbb92c43b17f26, 0xaa70b5b4f89695a2, 0xe94c39a54a98307f, 
      0xb7a0b174cff6f36e, 0xd4dba84729af48ad, 0x2e18bc1ad9704a68, 0x2de0966daf2f8b1c, 
      0xb9c11d5b1e43a07e, 0x64972d68dee33360, 0x94628d38d0c20584, 0xdbc0d2b6ab90a559, 
      0xd2733c4335c6a72f, 0x7e75d99d94a70f4d, 0x6ced1983376fa72b, 0x97fcaacbf030bc24, 
      0x7b77497b32503b12, 0x8547eddfb81ccb94, 0x79999cdff70902cb, 0xcffe1939438e9b24, 
      0x829626e3892d95d7, 0x92fae24291f2b3f1, 0x63e22c147b9c3403, 0xc678b6d860284a1c, 
      0x5873888850659ae7, 0x0981dcd296a8736d, 0x9f65789a6509a440, 0x9ff38fed72e9052f, 
      0xe479ee5b9930578c, 0xe7f28ecd2d49eecd, 0x56c074a581ea17fe, 0x5544f7d774b14aef, 
      0x7b3f0195fc6f290f, 0x12153635b2c0cf57, 0x7f5126dbba5e0ca7, 0x7a76956c3eafb413, 
      0x3d5774a11d31ab39, 0x8a1b083821f40cb4, 0x7b4a38e32537df62, 0x950113646d1d6e03, 
      0x4da8979a0041e8a9, 0x3bc36e078f7515d7, 0x5d0a12f27ad310d1, 0x7f9d1a2e1ebe1327, 
    ],
    [ 0xa09e8c8c35ab96de, 0xfa7e393983325753, 0xd6b6d0ecc617c699, 0xdfea21ea9e7557e3, 
      0xb67c1fa481680af8, 0xca1e3785a9e724e5, 0x1cfc8bed0d681639, 0xd18d8549d140caea, 
      0x4ed0fe7e9dc91335, 0xe4dbf0634473f5d2, 0x1761f93a44d5aefe, 0x53898e4c3910da55, 
      0x734de8181f6ec39a, 0x2680b122baa28d97, 0x298af231c85bafab, 0x7983eed3740847d5, 
      0x66c1a2a1a60cd889, 0x9e17e49642a3e4c1, 0xedb454e7badc0805, 0x50b704cab602c329, 
      0x4cc317fb9cddd023, 0x66b4835d9eafea22, 0x219b97e26ffc81bd, 0x261e4e4c0a333a9d, 
      0x1fe2cca76517db90, 0xd7504dfa8816edbb, 0xb9571fa04dc089c8, 0x1ddc0325259b27de, 
      0xcf3f4688801eb9aa, 0xf4f5d05c10cab243, 0x38b6525c21a42b0e, 0x36f60e2ba4fa6800, 
      0xeb3593803173e0ce, 0x9c4cd6257c5a3603, 0xaf0c317d32adaa8a, 0x258e5a80c7204c4b, 
      0x8b889d624d44885d, 0xf4d14597e660f855, 0xd4347f66ec8941c3, 0xe699ed85b0dfb40d, 
      0x2472f6207c2d0484, 0xc2a1e7b5b459aeb5, 0xab4f6451cc1d45ec, 0x63767572ae3d6174, 
      0xa59e0bd101731a28, 0x116d0016cb948f09, 0x2cf9c8ca052f6e9f, 0x0b090a7560a968e3, 
      0xabeeddb2dde06ff1, 0x58efc10b06a2068d, 0xc6e57a78fbd986e0, 0x2eab8ca63ce802d7, 
      0x14a195640116f336, 0x7c0828dd624ec390, 0xd74bbe77e6116ac7, 0x804456af10f5fb53, 
      0xebe9ea2adf4321c7, 0x03219a39ee587a30, 0x49787fef17af9924, 0xa1e9300cd8520548, 
      0x5b45e522e4b1b4ef, 0xb49c3b3995091a36, 0xd4490ad526f14431, 0x12a8f216af9418c2, 
    ],
    [ 0x6ffe73e81b637fb3, 0xddf957bc36d8b9ca, 0x64d0e29eea8838b3, 0x08dd9bdfd96b9f63, 
      0x087e79e5a57d1d13, 0xe328e230e3e2b3fb, 0x1c2559e30f0946be, 0x720bf5f26f4d2eaa, 
      0xb0774d261cc609db, 0x443f64ec5a371195, 0x4112cf68649a260e, 0xd813f2fab7f5c5ca, 
      0x660d3257380841ee, 0x59ac2c7873f910a3, 0xe846963877671a17, 0x93b633abfa3469f8, 
      0xc0c0f5a60ef4cdcf, 0xcaf21ecd4377b28c, 0x57277707199b8175, 0x506c11b9d90e8b1d, 
      0xd83cc2687a19255f, 0x4a29c6465a314cd1, 0xed2df21216235097, 0xb5635c95ff7296e2, 
      0x22af003ab672e811, 0x52e762596bf68235, 0x9aeba33ac6ecc6b0, 0x944f6de09134dfb6, 
      0x6c47bec883a7de39, 0x6ad047c430a12104, 0xa5b1cfdba0ab4067, 0x7c45d833aff07862, 
      0x5092ef950a16da0b, 0x9338e69c052b8e7b, 0x455a4b4cfe30e3f5, 0x6b02e63195ad0cf8, 
      0x6b17b224bad6bf27, 0xd1e0ccd25bb9c169, 0xde0c89a556b9ae70, 0x50065e535a213cf6, 
      0x9c1169fa2777b874, 0x78edefd694af1eed, 0x6dc93d9526a50e68, 0xee97f453f06791ed, 
      0x32ab0edb696703d3, 0x3a6853c7e70757a7, 0x31865ced6120f37d, 0x67fef95d92607890, 
      0x1f2b1d1f15f6dc9c, 0xb69e38a8965c6b65, 0xaa9119ff184cccf4, 0xf43c732873f24c13, 
      0xfb4a3d794a9a80d2, 0x3550c2321fd6109c, 0x371f77e76bb8417e, 0x6bfa9aae5ec05779, 
      0xcd04f3ff001a4778, 0xe3273522064480ca, 0x9f91508bffcfc14a, 0x049a7f41061a9e60, 
      0xfcb6be43a9f2fe9b, 0x08de8a1c7797da9b, 0x8f9887e6078735a1, 0xb5b4071dbfc73a66, 
    ],
    [ 0x55b6344cf97aafae, 0xb862225b055b6960, 0xcac09afbddd2cdb4, 0xdaf8e9829fe96b5f, 
      0xb5fdfc5d3132c498, 0x310cb380db6f7503, 0xe87fbb46217a360e, 0x2102ae466ebb1148, 
      0xf8549e1a3aa5e00d, 0x07a69afdcc42261a, 0xc4c118bfe78feaae, 0xf9f4892ed96bd438, 
      0x1af3dbe25d8f45da, 0xf5b4b0b0d2deeeb4, 0x962aceefa82e1c84, 0x046e3ecaaf453ce9, 
      0xf05d129681949a4c, 0x964781ce734b3c84, 0x9c2ed44081ce5fbd, 0x522e23f3925e319e, 
      0x177e00f9fc32f791, 0x2bc60a63a6f3b3f2, 0x222bbfae61725606, 0x486289ddcc3d6780, 
      0x7dc7785b8efdfc80, 0x8af38731c02ba980, 0x1fab64ea29a2ddf7, 0xe4d9429322cd065a, 
      0x9da058c67844f20c, 0x24c0e332b70019b0, 0x233003b5a6cfe6ad, 0xd586bd01c5c217f6, 
      0x5e5637885f29bc2b, 0x7eba726d8c94094b, 0x0a56a5f0bfe39272, 0xd79476a84ee20d06, 
      0x9e4c1269baa4bf37, 0x17efee45b0dee640, 0x1d95b0a5fcf90bc6, 0x93cbe0b699c2585d, 
      0x65fa4f227a2b6d79, 0xd5f9e858292504d5, 0xc2b5a03f71471a6f, 0x59300222b4561e00, 
      0xce2f8642ca0712dc, 0x7ca9723fbb2e8988, 0x2785338347f2ba08, 0xc61bb3a141e50e8c, 
      0x150f361dab9dec26, 0x9f6a419d382595f4, 0x64a53dc924fe7ac9, 0x142de49fff7a7c3d, 
      0x0c335248857fa9e7, 0x0a9c32d5eae45305, 0xe6c42178c4bbb92e, 0x71f1ce2490d20b07, 
      0xf1bcc3d275afe51a, 0xe728e8c83c334074, 0x96fbf83a12884624, 0x81a1549fd6573da5, 
      0x5fa7867caf35e149, 0x56986e2ef3ed091b, 0x917f1dd5f8886c61, 0xd20d8c88c8ffe65f, 
    ],
  ],
  [
    [ 0x0000000000000000 ] * 64,
    [ 0x9d39247e33776d41, 0x2af7398005aaa5c7, 0x44db015024623547, 0x9c15f73e62a76ae2, 
      0x75834465489c0c89, 0x3290ac3a203001bf, 0x0fbbad1f61042279, 0xe83a908ff2fb60ca, 
      0x0d7e765d58755c10, 0x1a083822ceafe02d, 0x9605d5f0e25ec3b0, 0xd021ff5cd13a2ed5, 
      0x40bdf15d4a672e32, 0x011355146fd56395, 0x5db4832046f3d9e5, 0x239f8b2d7ff719cc, 
      0x05d1a1ae85b49aa1, 0x679f848f6e8fc971, 0x7449bbff801fed0b, 0x7d11cdb1c3b7adf0, 
      0x82c7709e781eb7cc, 0xf3218f1c9510786c, 0x331478f3af51bbe6, 0x4bb38de5e7219443, 
      0xaa649c6ebcfd50fc, 0x8dbd98a352afd40b, 0x87d2074b81d79217, 0x19f3c751d3e92ae1, 
      0xb4ab30f062b19abf, 0x7b0500ac42047ac4, 0xc9452ca81a09d85d, 0x24aa6c514da27500, 
      0x4c9f34427501b447, 0x14a68fd73c910841, 0xa71b9b83461cbd93, 0x03488b95b0f1850f, 
      0x637b2b34ff93c040, 0x09d1bc9a3dd90a94, 0x3575668334a1dd3b, 0x735e2b97a4c45a23, 
      0x18727070f1bd400b, 0x1fcbacd259bf02e7, 0xd310a7c2ce9b6555, 0xbf983fe0fe5d8244, 
      0x9f74d14f7454a824, 0x51ebdc4ab9ba3035, 0x5c82c505db9ab0fa, 0xfcf7fe8a3430b241, 
      0x3253a729b9ba3dde, 0x8c74c368081b3075, 0xb9bc6c87167c33e7, 0x7ef48f2b83024e20, 
      0x11d505d4c351bd7f, 0x6568fca92c76a243, 0x4de0b0f40f32a7b8, 0x96d693460cc37e5d, 
      0x42e240cb63689f2f, 0x6d2bdcdae2919661, 0x42880b0236e4d951, 0x5f0f4a5898171bb6, 
      0x39f890f579f92f88, 0x93c5b5f47356388b, 0x63dc359d8d231b78, 0xec16ca8aea98ad76, 
    ],
    [ 0x56436c9fe1a1aa8d, 0xefac4b70633b8f81, 0xbb215798d45df7af, 0x45f20042f24f1768, 
      0x930f80f4e8eb7462, 0xff6712ffcfd75ea1, 0xae623fd67468aa70, 0xdd2c5bc84bc8d8fc, 
      0x7eed120d54cf2dd9, 0x22fe545401165f1c, 0xc91800e98fb99929, 0x808bd68e6ac10365, 
      0xdec468145b7605f6, 0x1bede3a3aef53302, 0x43539603d6c55602, 0xaa969b5c691ccb7a, 
      0xa87832d392efee56, 0x65942c7b3c7e11ae, 0xded2d633cad004f6, 0x21f08570f420e565, 
      0xb415938d7da94e3c, 0x91b859e59ecb6350, 0x10cff333e0ed804a, 0x28aed140be0bb7dd, 
      0xc5cc1d89724fa456, 0x5648f680f11a2741, 0x2d255069f0b7dab3, 0x9bc5a38ef729abd4, 
      0xef2f054308f6a2bc, 0xaf2042f5cc5c2858, 0x480412bab7f5be2a, 0xaef3af4a563dfe43, 
      0x19afe59ae451497f, 0x52593803dff1e840, 0xf4f076e65f2ce6f0, 0x11379625747d5af3, 
      0xbce5d2248682c115, 0x9da4243de836994f, 0x066f70b33fe09017, 0x4dc4de189b671a1c, 
      0x51039ab7712457c3, 0xc07a3f80c31fb4b4, 0xb46ee9c5e64a6e7c, 0xb3819a42abe61c87, 
      0x21a007933a522a20, 0x2df16f761598aa4f, 0x763c4a1371b368fd, 0xf793c46702e086a0, 
      0xd7288e012aeb8d31, 0xde336a2a4bc1c44b, 0x0bf692b38d079f23, 0x2c604a7a177326b3, 
      0x4850e73e03eb6064, 0xcfc447f1e53c8e1b, 0xb05ca3f564268d99, 0x9ae182c8bc9474e8, 
      0xa4fc4bd4fc5558ca, 0xe755178d58fc4e76, 0x69b97db1a4c03dfe, 0xf9b5b7c4acc67c96, 
      0xfc6a82d64b8655fb, 0x9c684cb6c4d24417, 0x8ec97d2917456ed0, 0x6703df9d2924e97e, 
    ],
    [ 0x7f9b6af1ebf78baf, 0x58627e1a149bba21, 0x2cd16e2abd791e33, 0xd363eff5f0977996, 
      0x0ce2a38c344a6eed, 0x1a804aadb9cfa741, 0x907f30421d78c5de, 0x501f65edb3034d07, 
      0x37624ae5a48fa6e9, 0x957baf61700cff4e, 0x3a6c27934e31188a, 0xd49503536abca345, 
      0x088e049589c432e0, 0xf943aee7febf21b8, 0x6c3b8e3e336139d3, 0x364f6ffa464ee52e, 
      0xd60f6dcedc314222, 0x56963b0dca418fc0, 0x16f50edf91e513af, 0xef1955914b609f93, 
      0x565601c0364e3228, 0xecb53939887e8175, 0xbac7a9a18531294b, 0xb344c470397bba52, 
      0x65d34954daf3cebd, 0xb4b81b3fa97511e2, 0xb422061193d6f6a7, 0x071582401c38434d, 
      0x7a13f18bbedc4ff5, 0xbc4097b116c524d2, 0x59b97885e2f2ea28, 0x99170a5dc3115544, 
      0x6f423357e7c6a9f9, 0x325928ee6e6f8794, 0xd0e4366228b03343, 0x565c31f7de89ea27, 
      0x30f5611484119414, 0xd873db391292ed4f, 0x7bd94e1d8e17debc, 0xc7d9f16864a76e94, 
      0x947ae053ee56e63c, 0xc8c93882f9475f5f, 0x3a9bf55ba91f81ca, 0xd9a11fbb3d9808e4, 
      0x0fd22063edc29fca, 0xb3f256d8aca0b0b9, 0xb03031a8b4516e84, 0x35dd37d5871448af, 
      0xe9f6082b05542e4e, 0xebfafa33d7254b59, 0x9255abb50d532280, 0xb9ab4ce57f2d34f3, 
      0x693501d628297551, 0xc62c58f97dd949bf, 0xcd454f8f19c5126a, 0xbbe83f4ecc2bdecb, 
      0xdc842b7e2819e230, 0xba89142e007503b8, 0xa3bc941d0a5061cb, 0xe9f6760e32cd8021, 
      0x09c7e552bc76492f, 0x852f54934da55cc9, 0x8107fccf064fcf56, 0x098954d51fff6580, 
    ],
    [ 0xda3a361b1c5157b1, 0xdcdd7d20903d0c25, 0x36833336d068f707, 0xce68341f79893389, 
      0xab9090168dd05f34, 0x43954b3252dc25e5, 0xb438c2b67f98e5e9, 0x10dcd78e3851a492, 
      0xdbc27ab5447822bf, 0x9b3cdb65f82ca382, 0xb67b7896167b4c84, 0xbfced1b0048eac50, 
      0xa9119b60369ffebd, 0x1fff7ac80904bf45, 0xac12fb171817eee7, 0xaf08da9177dda93d, 
      0x1b0cab936e65c744, 0xb559eb1d04e5e932, 0xc37b45b3f8d6f2ba, 0xc3a9dc228caac9e9, 
      0xf3b8b6675a6507ff, 0x9fc477de4ed681da, 0x67378d8eccef96cb, 0x6dd856d94d259236, 
      0xa319ce15b0b4db31, 0x073973751f12dd5e, 0x8a8e849eb32781a5, 0xe1925c71285279f5, 
      0x74c04bf1790c0efe, 0x4dda48153c94938a, 0x9d266d6a1cc0542c, 0x7440fb816508c4fe, 
      0x13328503df48229f, 0xd6bf7baee43cac40, 0x4838d65f6ef6748f, 0x1e152328f3318dea, 
      0x8f8419a348f296bf, 0x72c8834a5957b511, 0xd7a023a73260b45c, 0x94ebc8abcfb56dae, 
      0x9fc10d0f989993e0, 0xde68a2355b93cae6, 0xa44cfe79ae538bbe, 0x9d1d84fcce371425, 
      0x51d2b1ab2ddfb636, 0x2fd7e4b9e72cd38c, 0x65ca5b96b7552210, 0xdd69a0d8ab3b546d, 
      0x604d51b25fbf70e2, 0x73aa8a564fb7ac9e, 0x1a8c1e992b941148, 0xaac40a2703d9bea0, 
      0x764dbeae7fa4f3a6, 0x1e99b96e70a9be8b, 0x2c5e9deb57ef4743, 0x3a938fee32d29981, 
      0x26e6db8ffdf5adfe, 0x469356c504ec9f9d, 0xc8763c5b08d1908c, 0x3f6c6af859d80055, 
      0x7f7cc39420a3a545, 0x9bfb227ebdf4c5ce, 0x89039d79d6fc5c5c, 0x8fe88b57305e2ab6, 
    ],
    [ 0x001f837cc7350524, 0x1877b51e57a764d5, 0xa2853b80f17f58ee, 0x993e1de72d36d310, 
      0xb3598080ce64a656, 0x252f59cf0d9f04bb, 0xd23c8e176d113600, 0x1bda0492e7e4586e, 
      0x21e0bd5026c619bf, 0x3b097adaf088f94e, 0x8d14dedb30be846e, 0xf95cffa23af5f6f4, 
      0x3871700761b3f743, 0xca672b91e9e4fa16, 0x64c8e531bff53b55, 0x241260ed4ad1e87d, 
      0x106c09b972d2e822, 0x7fba195410e5ca30, 0x7884d9bc6cb569d8, 0x0647dfedcd894a29, 
      0x63573ff03e224774, 0x4fc8e9560f91b123, 0x1db956e450275779, 0xb8d91274b9e9d4fb, 
      0xa2ebee47e2fbfce1, 0xd9f1f30ccd97fb09, 0xefed53d75fd64e6b, 0x2e6d02c36017f67f, 
      0xa9aa4d20db084e9b, 0xb64be8d8b25396c1, 0x70cb6af7c2d5bcf0, 0x98f076a4f7a2322e, 
      0xbf84470805e69b5f, 0x94c3251f06f90cf3, 0x3e003e616a6591e9, 0xb925a6cd0421aff3, 
      0x61bdd1307c66e300, 0xbf8d5108e27e0d48, 0x240ab57a8b888b20, 0xfc87614baf287e07, 
      0xef02cdd06ffdb432, 0xa1082c0466df6c0a, 0x8215e577001332c8, 0xd39bb9c3a48db6cf, 
      0x2738259634305c14, 0x61cf4f94c97df93d, 0x1b6baca2ae4e125b, 0x758f450c88572e0b, 
      0x959f587d507a8359, 0xb063e962e045f54d, 0x60e8ed72c0dff5d1, 0x7b64978555326f9f, 
      0xfd080d236da814ba, 0x8c90fd9b083f4558, 0x106f72fe81e2c590, 0x7976033a39f7d952, 
      0xa4ec0132764ca04b, 0x733ea705fae4fa77, 0xb4d8f77bc3e56167, 0x9e21f4f903b33fd9, 
      0x9d765e419fb69f6d, 0xd30c088ba61ea5ef, 0x5d94337fbfaf7f5b, 0x1a4e4822eb4d7a59, 
    ],
    [ 0x230e343dfba08d33, 0x43ed7f5a0fae657d, 0x3a88a0fbbcb05c63, 0x21874b8b4d2dbc4f, 
      0x1bdea12e35f6a8c9, 0x53c065c6c8e63528, 0xe34a1d250e7a8d6b, 0xd6b04d3b7651dd7e, 
      0x5e90277e7cb39e2d, 0x2c046f22062dc67d, 0xb10bb459132d0a26, 0x3fa9ddfb67e2f199, 
      0x0e09b88e1914f7af, 0x10e8b35af3eeab37, 0x9eedeca8e272b933, 0xd4c718bc4ae8ae5f, 
      0x81536d601170fc20, 0x91b534f885818a06, 0xec8177f83f900978, 0x190e714fada5156e, 
      0xb592bf39b0364963, 0x89c350c893ae7dc1, 0xac042e70f8b383f2, 0xb49b52e587a1ee60, 
      0xfb152fe3ff26da89, 0x3e666e6f69ae2c15, 0x3b544ebe544c19f9, 0xe805a1e290cf2456, 
      0x24b33c9d7ed25117, 0xe74733427b72f0c1, 0x0a804d18b7097475, 0x57e3306d881edb4f, 
      0x4ae7d6a36eb5dbcb, 0x2d8d5432157064c8, 0xd1e649de1e7f268b, 0x8a328a1cedfe552c, 
      0x07a3aec79624c7da, 0x84547ddc3e203c94, 0x990a98fd5071d263, 0x1a4ff12616eefc89, 
      0xf6f7fd1431714200, 0x30c05b1ba332f41c, 0x8d2636b81555a786, 0x46c9feb55d120902, 
      0xccec0a73b49c9921, 0x4e9d2827355fc492, 0x19ebb029435dcb0f, 0x4659d2b743848a2c, 
      0x963ef2c96b33be31, 0x74f85198b05a2e7d, 0x5a0f544dd2b1fb18, 0x03727073c2e134b1, 
      0xc7f6aa2de59aea61, 0x352787baa0d7c22f, 0x9853eab63b5e0b35, 0xabbdcdd7ed5c0860, 
      0xcf05daf5ac8d77b0, 0x49cad48cebf4a71e, 0x7a4c10ec2158c4a6, 0xd9e92aa246bf719e, 
      0x13ae978d09fe5557, 0x730499af921549ff, 0x4e4b705b92903ba4, 0xff577222c14f0a3a, 
    ],
  ],
]

epHashes = [0x70cc73d90bc26e24, 0xe21a6b35df0c3ad7, 0x003a93d8b2806962, 0x1c99ded33cb890a1, 
            0xcf3145de0add4289, 0xd0e4427a5514fb72, 0x77c621cc9fb3a483, 0x67a34dac4356550b ]

W_OOHash  = 0x31d71dce64b2c310
W_OOOHash = 0xf165b587df898190
B_OOHash  = 0xa57e6339dd2cf3a0
B_OOOHash = 0x1ef6e6dbb1961ec9

colorHash = 0xf8d626aaaf278509
