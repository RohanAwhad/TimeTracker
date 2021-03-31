var start_secs = null;
var end_secs = null;
var activity_name = "";

$("#start_timer").click(evt => {
    start_secs = Math.floor(Date.now() / 1000)
    console.log(start_secs)
})

$("#end_timer").click(evt => {
    if (start_secs !== null){
        end_secs = Math.floor(Date.now() / 1000)
        console.log(end_secs)

        activity_name = $("#activity").val()
        if (activity_name !== ""){
            start = new Date(start_secs * 1000).toLocaleTimeString()
            end = new Date(end_secs * 1000).toLocaleTimeString()
        
            $('#from_span').val(start)
            $('#to_span').val(end)
            $('#activity_span').val(activity_name)
        }
        else {
            alert('Add activity name before ending timer')
        }
    }
})

$("#save").click(evt => {
    // start = new Date(start_secs * 1000).toLocaleTimeString()
    // end = new Date(end_secs * 1000).toLocaleTimeString()
    // console.log("from ", start, "to", end, activity_name)

    const save_data = {
        activity: activity_name,
        start: new Date(start_secs * 1000),
        end: new Date(end_secs * 1000)
    }

    db.collection('time_spent').add(save_data)

    start_secs = null
    end_secs = null
    $('#activity').val("")
})