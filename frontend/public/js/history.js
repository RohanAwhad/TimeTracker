const rowHTML = `<div class="row mt-3" id="activity_id">
<div class="col">
    Date: <span>date</span>
</div>
<div class="col">
    Activity: <span>activity_name</span>
</div>
<div class="col">
    From: <span>from_timer</span>
</div>
<div class="col">
    To: <span>to_timer</span>
</div>
<div class="col">
    Time Spent: <span>time_spent</span>
</div>
</div>`

const renderRow = (activity_name, from, to, id, date, time_spent) => {
    earlier_html = $('#container').html() 
    var this_row = rowHTML.replace("activity_id", id)
    this_row = this_row.replace('date', date)
    this_row = this_row.replace('activity_name', activity_name)
    this_row = this_row.replace('from_timer', from)
    this_row = this_row.replace('to_timer', to)
    this_row = this_row.replace('time_spent', time_spent)

    $('#container').html(this_row + earlier_html)
}

db.collection('time_spent').onSnapshot(snapshot => {
    snapshot.docChanges().forEach(change => {
        console.log(change, change.doc.data(), change.doc.id)
        if (change.type === 'added'){
            var id = change.doc.id
            var data = change.doc.data()
            var start = data['start']['seconds'] * 1000
            var end = data['end']['seconds'] * 1000

            var activity_name = data['activity']
            var date = new Date(start).toLocaleDateString()
            var from = new Date(start).toLocaleTimeString().slice(0, -3)
            var to = new Date(end).toLocaleTimeString().slice(0, -3)
            var time_spent = new Date(end-start).toISOString().substr(11, 8)

            renderRow(activity_name, from, to, id, date, time_spent)
        }
        if (change.type === 'removed'){
            $('#'+change.doc.id).remove()
        }
    });
})