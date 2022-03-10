let upvotebtn = document.querySelector('#upvote');
let downvotebtn = document.querySelector('#downVote');

let input1 = document.querySelector('#input1')
let input2 = document.querySelector('#input2')

upvotebtn.addEventListener('click', () => {
    input1.value = parseInt(input1.value) + 1;
})
downvotebtn.addEventListener('click', () => {
    input2.value = parseInt(input2.value) + 1;
})
