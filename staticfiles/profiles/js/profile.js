let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
    $('#id_default_country').css('fontFamily', '"Raleway", sans-serif');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
        $(this).css('fontFamily', '"Raleway", sans-serif');
    } else {
        $(this).css('color', '#000');
        $(this).css('fontFamily', '"Raleway", sans-serif');
    }
});
