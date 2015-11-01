function getAge(){
    str = $("#ic_no").val();

    first = str.charAt(0);
    yy = str.substring(0,2);
    currentYear = 2015;

    if(first == 0) {
        age = 15 - yy
    } else {
        yyyy = "19" + yy;
        age = currentYear - yyyy;
    }
    console.log(age);
    $("#age").val(age);
    return age;
}
