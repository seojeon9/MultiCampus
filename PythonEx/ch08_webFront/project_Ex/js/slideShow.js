/*
* slideShow.js
*/

$(function(){
    //현재 이미지의 index값 저장 변수 생성
    var moveIndex = 0;

    //슬라이드 패널을 움직여주는 사용자 정의 함수
    function moveSlide(index){
        //전달받은 index 값ㅇ을 다른 변수(전역변수)에 저장
        moveIndex = index;

        //슬라이드 이동 거리 계산
        var moveLeft = -(index * 1280) //왼쪽으로 이동거리
        $('#slidePanel').animate({'left':moveLeft},'slow');
    }

    //prev 버튼 클릭 : 앞 이미지로 이동
    $('#prevButton').on('click',function(){

    });
    //next 버튼 클릭 : 뒤 이미지로 이동
    $('#nextButton').on('click',function(){

    });
});

