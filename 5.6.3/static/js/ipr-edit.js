function cloneMore(selector, type) {
    var newElement = jQuery(selector).clone(true);
    var total = jQuery('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = jQuery(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        jQuery(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = jQuery(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        jQuery(this).attr('for', newFor);
    });
    jQuery(selector).find('a[id$="add_link"]').remove();
    total++;
    jQuery('#id_' + type + '-TOTAL_FORMS').val(total);
    jQuery(selector).after(newElement);
}

jQuery(function() {
    jQuery('#draft_add_link').click(function() {
        cloneMore('#id_contribution tr.draft_row:last','draft');
    });
    jQuery('#rfc_add_link').click(function() {
        cloneMore('#id_contribution tr.rfc_row:last','rfc');
    });
    
    //$('input.draft-autocomplete').autocomplete({
    //    source: "/doc/ajax/internet_draft/?",
    //    minLength: 3,
    //});

})