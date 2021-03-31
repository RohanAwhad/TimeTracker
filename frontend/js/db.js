// db.collection('time_spent').onSnapshot(snapshot => {
//     snapshot.docChanges().forEach(change => {
//         console.log(change, change.doc.data(), change.doc.id)
//         if (change.type === 'added'){
//             var id = change.doc.id
//             var data = change.doc.data()
//             var activity_name = data['activity']
//             var date = new Date(data['start']['seconds'] * 1000).toLocaleDateString()
//             var from = new Date(data['start']['seconds'] * 1000).toLocaleTimeString()
//             var to = new Date(data['end']['seconds'] * 1000).toLocaleTimeString()


//         }
//         if (change.type === 'removed'){

//         }
//     });
// })