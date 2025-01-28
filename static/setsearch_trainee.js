const searchfield= document.querySelector('#searchfield')
const tablehead=document.querySelector('.table-head')
const tablebody=document.querySelector(".trainee-table-body")
const noResults = document.querySelector('#no-results');
const paginationContainer=document.querySelector(".pagination-container")
const tablecomplete=document.querySelector(".table-complete")
const data=tablebody.innerHTML;

// tablehead.style.display='none';
searchfield.addEventListener("keyup",(e)=>{
    const searchvalue=e.target.value.trim();
    if(searchvalue.length>0){
        paginationContainer.style.display="none"
        fetch("/trainee_search",{
            body: JSON.stringify({searchtext:searchvalue}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("data",data)
            tablebody.innerHTML = '';
            tablehead.style.display = 'block';
            noResults.style.display = data.length === 0 ? 'block' : 'none';
            data.forEach((trainee, index) => {
                tablebody.innerHTML += `
                    <tr>
                        <td>${index + 1}</td>
                        <td>${trainee.name}</td>
                        <td>${trainee.phone}</td>
                        <td>${trainee.email}</td>
                        <td>${trainee.course}</td>
                        <td>${trainee.domain}</td>
                        <td>
                            <a href="#editEmployeeModal-${index + 1}" class="edit" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Edit">&#xE254;</i></a>
                            <a href="#deleteEmployeeModal-${index + 1}" class="delete" data-toggle="modal"><i class="material-icons" data-toggle="tooltip" title="Delete">&#xE872;</i></a>
                        </td>
                    </tr>`;
                });
        })
    }
    else {
        tablebody.innerHTML=data;
        paginationContainer.style.display="block";
    }

})
