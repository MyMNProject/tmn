environments = {
    'testnet': {
        'tomochain': {
            'BOOTNODES': (
                'enode://4d3c2cc0ce7135c1778c6f1cfda623ab44b4b6db55289543d48ec'
                'fde7d7111fd420c42174a9f2fea511a04cf6eac4ec69b4456bfaaae0e5bd2'
                '36107d3172b013@52.221.28.223:30301,enode://298780104303fcdb37'
                'a84c5702ebd9ec660971629f68a933fd91f7350c54eea0e294b0857f1fd2e'
                '8dba2869fcc36b83e6de553c386cf4ff26f19672955d9f312@13.251.101.'
                '216:30301,enode://46dba3a8721c589bede3c134d755eb1a38ae7c5a4c6'
                '9249b8317c55adc8d46a369f98b06514ecec4b4ff150712085176818d18f5'
                '9a9e6311a52dbe68cff5b2ae@13.250.94.232:30301'
            ),
            'NETSTATS_HOST': 'stats.testnet.tomochain.com',
            'NETSTATS_PORT': '443',
            'NETWORK_ID': '89',
            'WS_SECRET': (
                'anna-coal-flee-carrie-zip-hhhh-tarry-laue-felon-rhine'
            )
        },
        'metrics': {
            'METRICS_ENDPOINT': 'https://metrics.testnet.tomochain.com'
        }
    },
    'devnet': {
        'tomochain': {
            'BOOTNODES': (
                'enode://f3d3d5d6cd0fdde8996722ff5b5a92f331029b2dcbdb9748f50db'
                '1421851a939eb660bf81a7ec7f359454aa0fd65fe4c03ae5c6bb2382b34df'
                'aaca7eb6ecaf4e@52.77.194.164:30301,enode://34b923ddfcba1bfafd'
                'd1ac7a030436f9fbdc565919189f5e62c8cadd798c239b5807a26ab7f6b96'
                'a44200eb0399d1ebc2d9c1be94d2a774c8cc7660ff4c10367@13.228.93.2'
                '32:30301,enode://e2604862d18049e025f294d63d537f9f54309ff09e45'
                'ed69ff4f18c984831f5ef45370053355301e3a4da95aba2698c6116f4d2a3'
                '47e5a5e0a3152ac0ae0f574@18.136.42.72:30301'
            ),
            'NETSTATS_HOST': 'stats.devnet.tomochain.com',
            'NETSTATS_PORT': '443',
            'NETWORK_ID': '90',
            'WS_SECRET': (
                'torn-fcc-caper-drool-jelly-zip-din-fraud-rater-darn'
            )
        },
        'metrics': {
            'METRICS_ENDPOINT': 'https://metrics.devnet.tomochain.com'
        }
    }
}
