signature = 0x929c83f4a5116ec613d5d94233cd5d77776b9b04b9eb9fd3eb384ff76f8607fd4294d8a6feff7300861f983866fea3b3977d83c3675d6214495cdb09be72e588383ac665a26225de9b84a91119b69689e5dded1ea078f136de816f50f8ac034db52c055615afe45760c1531e238441705701f5697b49fec279f9ed63c977d9f29a86aecc959bc4d8fca6945283393c6ae3d353ed2bb0bbf48c858713ca59bd2da79e449d0e7a9e030dbc8aa7c8178627837e2733041837bcac4bed7ec5f5397cd70baa6c412e8296f9e569c22447209c639821679b38da5e7d2c429adac352b49b93b53392c99498621c7ef90f9087e4f5500ce26ec834ad148bfa6438b2de96

modulus = 0x00bb021528ccf6a094d30f12ec8d5592c3f882f199a67a4288a75d26aab52bb9c54cb1af8e6bf975c8a3d70f4794145535578c9ea8a23919f5823c42a94e6ef53bc32edb8dc0b05cf35938e7edcf69f05a0b1bbec094242587fa3771b313e71cace19befdbe43b45524596a9c153ce34c852eeb5aeed8fde6070e2a554abb66d0e97a540346b2bd3bc66eb66347cfa6b8b8f572999f830175dba726ffb81c5add286583d17c7e709bbf12bf786dcc1da715dd446e3ccad25c188bc60677566b3f118f7a25ce653ff3a88b647a5ff1318ea9809773f9d53f9cf01e5f5a6701714af63a4ff99b3939ddc53a706fe48851da169ae2575bb13cc5203f5ed51a18bdb15

exponent = 65537

sha_sum_value = pow(signature, exponent, modulus)
print(f"{hex(sha_sum_value)}")