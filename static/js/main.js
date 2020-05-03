
(function(){
    var test = function(){
        console.log("Lol")
    }
    var showAll = function(){
        $("#showAll").click(()=>{
            console.log("clicked")
        })
    }
    $(function(){
        test();
        showAll();
    })
})()

function helloWorld(){
    console.log("HelloWorld")
}

function addCards(data){
    console.log(data)
}

