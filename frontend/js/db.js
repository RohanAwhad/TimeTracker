db.collection('time_spent').onSnapshot(snapshot => {
    snapshot.docChanges().forEach(change => {
        console.log(change, change.doc.data(), change.doc.id)
        if (change.type === 'added'){

        }
        if (change.type === 'removed'){

        }
    });
})