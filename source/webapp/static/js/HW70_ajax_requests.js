function getAllProjects(){
    $.ajax({
        url: 'http://localhost:9000/api/projects/',
        method: 'get',
        headers: {"Authorization": "Token bc4ac83cfbaae30c5ae1e99f3c8a451aa37d087a"},
        data: JSON.stringify({username: "admin", password: "admin"}),
        dataType: 'json',
        contentType: "application/json",
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });
}

function getAllIssues(){
    $.ajax({
        url: 'http://localhost:9000/api/issues/',
        method: 'get',
        headers: {"Authorization": "Token bc4ac83cfbaae30c5ae1e99f3c8a451aa37d087a"},
        data: JSON.stringify({username: "admin", password: "admin"}),
        dataType: 'json',
        contentType: "application/json",
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });
}

function getProjectIssues(){
    $.ajax({
        url: 'http://localhost:9000/api/projects/1/',
        method: 'get',
        headers: {"Authorization": "Token bc4ac83cfbaae30c5ae1e99f3c8a451aa37d087a"},
        data: JSON.stringify({username: "admin", password: "admin"}),
        dataType: 'json',
        contentType: "application/json",
        success: function(response, status){console.log(response);},
        error: function(response, status){console.log(response);}
    });
}

function createIssue(){
    $.ajax({
        url : 'http://localhost:9000/api/issues/',
        method: 'post',
        headers : {"Authorization" : "Token bc4ac83cfbaae30c5ae1e99f3c8a451aa37d087a"},
        data: JSON.stringify({summary: "Test", desctiption: "Test", status:1, type: 1, project: 1 , created_by: 1,
        assigned_to: 1}),
        contentType:"application/json",
        dataType : "json",
        success:function(response, status) {console.log(response);},
        error: function(response, status) {console.log(response);}
    });
}

function deleteIssue(){
    $.ajax({
        url : 'http://localhost:9000/api/issues/2',
        method: 'delete',
        headers : {"Authorization" : "Token bc4ac83cfbaae30c5ae1e99f3c8a451aa37d087a"},
        data: JSON.stringify({username: "admin", password: "admin"}),
        contentType:"application/json",
        dataType : "json",
        success:function(response, status) {console.log(response);},
        error: function(response, status) {console.log(response);}
    });
}

getAllProjects();
getAllIssues();
getProjectIssues();
createIssue();
deleteIssue();
