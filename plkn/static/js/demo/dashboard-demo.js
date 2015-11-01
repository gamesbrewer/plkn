$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2010 Q1',
            Combined: 2666,
            KK: null,
            Miri: 2647
        }, {
            period: '2010 Q2',
            Combined: 2778,
            KK: 2294,
            Miri: 2441
        }, {
            period: '2010 Q3',
            Combined: 4912,
            KK: 1969,
            Miri: 2501
        }, {
            period: '2010 Q4',
            Combined: 3767,
            KK: 3597,
            Miri: 5689
        }, {
            period: '2011 Q1',
            Combined: 6810,
            KK: 1914,
            Miri: 2293
        }, {
            period: '2011 Q2',
            Combined: 5670,
            KK: 4293,
            Miri: 1881
        }, {
            period: '2011 Q3',
            Combined: 4820,
            KK: 3795,
            Miri: 1588
        }, {
            period: '2011 Q4',
            Combined: 15073,
            KK: 5967,
            Miri: 5175
        }, {
            period: '2012 Q1',
            Combined: 10687,
            KK: 4460,
            Miri: 2028
        }, {
            period: '2012 Q2',
            Combined: 8432,
            KK: 5713,
            Miri: 1791
        }],
        xkey: 'period',
        ykeys: ['Combined', 'KK', 'Miri'],
        labels: ['Combined', 'KK', 'Miri'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: 'Melayu',
            a: 100,
            b: 90
        }, {
            y: 'Cina',
            a: 75,
            b: 65
        }, {
            y: 'India',
            a: 50,
            b: 40
        }, {
            y: 'Iban',
            a: 75,
            b: 65
        }, {
            y: 'Melanau',
            a: 50,
            b: 40
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Lelaki', 'Perempuan'],
        hideHover: 'auto',
        resize: true
    });

    Morris.Line({
        element: 'morris-line-chart',
        data: [{
            y: '2015',
            a: 100,
            b: 90
        }, {
            y: '2007',
            a: 75,
            b: 65
        }, {
            y: '2008',
            a: 50,
            b: 40
        }, {
            y: '2009',
            a: 75,
            b: 65
        }, {
            y: '2010',
            a: 50,
            b: 40
        }, {
            y: '2011',
            a: 75,
            b: 65
        }, {
            y: '2012',
            a: 100,
            b: 90
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: 'auto',
        resize: true
    });

    // Donut Chart
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Perempuan",
            value: 160
        }, {
            label: "Lelaki",
            value: 200
        }],
        resize: true
    });
});
