let sf = document.getElementById("sf");
let cust = document.getElementById("cust");
let my_img = document.querySelector("#my_img");
let fn = document.querySelector("#fn");

function uploadUrl(sendObj, end_point) {
    fetch("http://127.0.0.1:5000" + end_point, {
        body: JSON.stringify(sendObj),
        headers: {
            "Content-Type": "application/json",
        },
        method: "post"
    })
        .then((response) => response.json())
        .then((data) => {
            output.innerHTML = JSON.stringify(data);
            setTimeout(() => {
                output.innerHTML = ''
                // output.style.display = 'none';
            }, 2000);
        })
        .catch((err) => {
            output.innerHTML = JSON.stringify(err);
        });
}

var my_queue = [];

function get_data(end_point) {
    fetch("http://127.0.0.1:5000" + end_point, {
        body: JSON.stringify({
            'path': sf.value
        }),
        headers: {
            "Content-Type": "application/json",
        },
        method: "post"
    })
        .then((response) => response.json())
        .then((data) => {
            my_queue = data
            console.log(my_queue)
            my_img.style.backgroundImage = "url('img/" + sf.value + '/' + my_queue[0] + "')";
        })
        .catch((err) => {
            console.log(err);
            output.innerHTML = JSON.stringify(err);
        });
}

function get_data_api(end_point, sf, df, fn) {
    fetch("http://127.0.0.1:5000" + end_point, {
        body: JSON.stringify({
            'sf': sf,
            'df': df,
            'fn': fn
        }),
        headers: {
            "Content-Type": "application/json",
        },
        method: "post"
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data)
        })
        .catch((err) => {
            console.log(err);
            output.innerHTML = JSON.stringify(err);
        });
}
function move_file(df){
    if (1 < my_queue.length) {
        let fn = my_queue.shift()
        my_img.style.backgroundImage = "url('img/" + sf.value + '/' + my_queue[0] + "')";
        get_data_api('/move-file', sf.value, df, fn)
    } else if (1 === my_queue.length) {
        let fn = my_queue.shift()
        my_img.style.backgroundImage = "url('img/no_img.jpg')";
        get_data_api('/move-file', sf.value, df, fn)
    } else {
        my_img.style.backgroundImage = "url('img/no_img.jpg')";
        console.log('queue is empty')
    }
}



