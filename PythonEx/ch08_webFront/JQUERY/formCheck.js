//formCheck.js
//회원가입 폼 입력

$(document).ready(function(){

    //문서 로드 후 id 입력창에 포커스
    $('#id').focus();

    //아이디와 비밀번호 입력란에 포커스가 있을 때 배경 색상 변경
    //focus, blur 이벤트
    $('input[type="text"],input[type="password"]').on('focus',function(){
        $(this).css('background','rgb(232,232,232)')
    });

    //아이디와 비밀번호 입력란에 포커스가 없어지면 배경 색상 변경
    $(':text,:password').on('blur',function(){
        $(this).css('background','rgb(255,255,255)')
    });

    //키보드 이벤트 = 휴대폰 입력란에서 입력 값 개수 확인
    //첫번째 번호 입력란에서 입력값이 3개가 되면 포커스 이동
    $('#hp1').on('keyup',function(){
        if($(this).val().length==3){
            $("#hp2").focus();
        }
    });

    //두번째 번호 입력란에서 입력값이 4개가 되면 포커스 이동
    $('#hp2').on('keyup',function(){
        if($(this).val().length==4){
            $("#hp3").focus();
        }
    });

    //submit 이벤트 : submit 버튼 클릭시 발생, FORM 태그(input 등) 위에서 enter 키를 누르면 발생
    //enter키를 눌렀을 때 무조건 submit 안되도록
    //문서 전체에 이벤트 처리
    //[Enter]키의 아스키코드값 : 13
    //fuction(e) : 파라미터 변수를 설정하면 발생된 이벤트에 대한 정보를 받을 수 있음
    $(document).on('keydown',function(e){
        if(e.keyCode == 13) return false;
    });

    //id 입력후 엔터키 눌렀을 때 비밀번호로 포커스 이동
    $('#id').on('keydown',function(e){
        if($('#id').val()!="" && e.keyCode==13)
            $('#pwd').focus();
    });

    // 회원가입 폼 입력 유효성을 확인하는 시점-전송버튼 클릭시(submit 이벤트가 발생)
    // submit 이벤트는 form 태그에 연결해야 함
    $('#newMemberForm').on('submit',function(){
       if($('#id').val()==""){ //아이디를 입력하지 않은 경우
           alert("아이디를 입력하세요.");
           $('#id').focus();
           return false; //서버로 전송되지 않도록 전송 기능 막음
       }

       if($('#pwd').val()==""){ //비밀번호 입력하지 않은 경우
           alert("비밀번호를 입력하세요.");
           $('#pwd').focus();
           return false;
       }

       if(!$('input[type="radio"]').is(':checked')){ //라디오버튼(학년) 선택하지 않은 경우
           alert('학년을 선택하세요.');
           return false;
       }

       if(!$('input[type="checkbox"]').is(':checked')){
            alert('관심분야는 1개 이상 선택하세요.');
            return false;
       }
       
       if($('select').val()==""){
        alert("학과를 선택하세요.");
        $('select').focus();
        return false;
       }
       
    });//폼 submit on 끝


});//ready 끝
