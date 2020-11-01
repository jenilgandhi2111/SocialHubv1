$(document).ready(function () {
    $('.commentsslide').slideUp(1)
    $('.comment').click(
        function () {
            var id = this.id
            id = String(id)
            var final_id = id.match(/\d+/g);
            console.log(final_id[0]);
            var myKeyVals = { 'post_id': this.id }

            $('#' + 'comment' + final_id[0]).slideToggle(400)
            var saveData = $.ajax({
                type: 'POST',
                url: "http://127.0.0.1:8000/home/comments/",
                data: myKeyVals,
                dataType: "text",
                success: function (resultData) { console.log(JSON.parse(resultData)['comments'][0]); }
            });
            saveData.error(function () { alert("Something went wrong"); });
        }
    )

    $('.heart_target').click(function () {
        //toggling the heart button
        if (this.classList.contains('far')) {
            this.classList.remove('far')
            this.classList.add('fas')
            console.log(this.id)
            const todo = {
                title: 'Some really important work to finish'
            };
            var hid=this.id;
            var dat=hid.match(/\d+/g)[0]
            var target_post=document.getElementById("pid"+dat)
            console.log(target_post);
            var author_name=target_post.children[0].children[1].children[0].children[0].innerText
            console.log(author_name);
            var liker=document.getElementById("usnm").innerText
            console.log(liker);
            //send a fetch api request saying user having userid = this has liked the post
            var myKeyVals = { 'author_name':author_name, 'liker_name': liker, 'time_liked': Date.now(), 'post_liked': dat }



            var saveData = $.ajax({
                type: 'POST',
                url: "http://127.0.0.1:8000/home/like/",
                data: myKeyVals,
                dataType: "text",
                success: function (resultData) { console.log("Post liked"); }
            });
            saveData.error(function () { alert("Something went wrong"); });
        }
        else {
            this.classList.remove('fas')
            this.classList.add('far')
            var hid=this.id;
            var dat=hid.match(/\d+/g)[0]
            var target_post=document.getElementById("pid"+dat)
            console.log(target_post);
            var auth_name=target_post.children[0].children[1].children[0].children[0].innerText
            console.log(auth_name);
            var unliker=document.getElementById("usnm").innerText
            console.log(unliker);
            var myKeyVals = { 'author_name': auth_name, 'unliker_name': unliker, 'time_unliked': Date.now(), 'post_unliked': dat }
            


            var saveData = $.ajax({
                type: 'POST',
                url: "http://127.0.0.1:8000/home/unlike/",
                data: myKeyVals,
                dataType: "text",
                success: function (resultData) {
                    console.log("Post unliked");

                }
            });
            saveData.error(function () { alert("Something went wrong"); });

            //send a fetch api request saying user has disliked the post 
        }
    })
}
)
