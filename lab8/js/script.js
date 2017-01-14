$(function() {
    var $from = $('.from');
    var $to = $('.to');
    var $func = $('.func');
    var $button = $('.btn');
    var $output = $('.output');
    var $stop = $('.stop');

    $button.click(function () {
        $stop.show();
        var begin = parseFloat($from.val());
        var end = parseFloat($to.val());
        var func = $func.val();
        var point = [];
        var dx = (end-begin)/20;

        var dynamic = setInterval(function () {
            for (var x = begin; x<=end; x+=0.1) {
                var y = eval(func);
                point.push([x,y]);
            }

            var points = [{data: point, label: func}];
            $.plot($output, points, {});

            begin += dx;
            end += dx;
            point = [];
        }, 100);

        $stop.click(function () {
            clearInterval(dynamic);
        })
    });
});