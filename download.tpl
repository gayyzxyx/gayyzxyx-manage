<!DOCTYPE html>
<html>
<head>
    <title>download page</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="expires" content="0" />
    <link rel="stylesheet" href="/static/css/style.css" />
    <link rel="stylesheet" href="/static/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/static/css/bootstrap-responsive.min.css" />
    <link rel="stylesheet" href="/static/css/zTreeStyle.css" />
    <link rel="shortcut icon" href="/static/favicon.ico" />
    <script type="text/javascript" src="/static/js/jquery-1.7.2.min.js"></script>
    <script type="text/javascript" src="/static/js/bootstrap.js"></script>
    <script src="//cdnjs.bootcss.com/ajax/libs/html5shiv/3.6.2/html5shiv.js"></script>
    <script type = "text/javascript" src="/static/js/jquery-1.7.2.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    <script src="/static/js/bootstrap-modal.js"></script>
    <script type="text/javascript" src="/static/js/bootstrap-tab.js"></script>
    <script type="text/javascript" src="/static/js/bootstrap-dropdown.js"></script>
    <script type="text/javascript" src="/static/js/bootstrap-tooltip.js"></script>
</head>
<body>
<div class="container">
    <div class="tabbable">
        <ul class="nav nav-tabs" id="myTab">
            <li class="active"><a href="#file-download" data-toggle="tab">File Manager</a></li>
            <li><a href="#admin" data-toggle="tab">Admin</a></li>
        </ul>
        <div class="tab-content">
            <div class="tab-pane active in fade" id="file-download">
                <form class="form-search" action="/download" method="post">
                    <h2 style="margin-bottom: 10px">File Address:</h2>
                    <div class="input-append">
                        <input type="text" class="input-xxlarge" id="down_address" name="down_address">
                        <button type="submit" class="btn">download</button>
                    </div>
                </form>
                <table class="table table-bordered table-hover table-striped">
                    <thead>
                    <tr>
                        <td style="word-wrap: break-word" width="60%"><p class="lead text-center">File Name</p></td>
                        <td style="word-wrap: break-word" width="20%"><p class="lead text-center">File Size</p> </td>
                        <td style="word-wrap: break-word" width="20%"><p class="lead text-center">Operation</p></td>
                    </tr>
                    </thead>
                    %for file in filelist:
                    <tr>
                        <td id="filename">{{file.fileName}}</td>
                        <td>
                            % if file.status == '100':
                                {{file.fileSize/1024.0/1024.0}}MB
                            % else:
                            <div class="progress progress-striped active">
                                <div class="bar" style="width:{{file.status}}%;"></div>
                            </div>

                            % end

                        </td>
                        <td style="text-align: center">
                            <div class="btn-group">
                                <button class="btn">Action</button>
                                <button class="btn dropdown-toggle" data-toggle="dropdown">
                                    <span class="caret"></span>
                                </button>
                                <ul class="dropdown-menu">
                                    <li><a href="#" onclick='deleteFile("{{file.fileName}}")' data-toggle="popver" data-placement="right" title data-original-title="Attention">delete</a></li>
                                    <li><a href="#" onclick='getFileName("{{file.fileName}}")' data-toggle="modal" role="button">rename</a></li>
                                </ul>
                            </div>
                        </td>
                    </tr>
                    %end
                </table>
                <div class="pagination pagination-small pagination-right">
                    <ul id="pagination">
                        <input type="hidden" id="curpage" value={{curpage}}>
                        <input type="hidden" id="total" value={{total/10+1}}>
                        <li><a href="/getfile/{{curpage-1}}" id="Prev">Prev</a></li>
                        %for i in range(0,total/10+1):
                        <li><a href="/getfile/{{i+1}}" id="page">{{i+1}}</a></li>
                        %end
                        <li><a href="/getfile/{{curpage+1}}" id="Next">Next</a></li>
                    </ul>
                </div>
            </div>
            <div class="tab-pane fade" id="admin">
                <div class="row">
                    <div class="span4">
                        <ul class="thumbnails">
                            <li class="span4">
                                <div class="thumbnail">
                                    <img src="/static/yaoxin.jpg" alt="Can't show now">

                                    <p class="text-center">
                                        <button class="btn btn-primary" type="button">Capture</button>
                                        <button class="btn" type="button">Download</button>
                                    </p>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div class="span5">
                        <div class="input-append">
                            <input type="text" value={{fileLocation}} id="fileLocation" >
                            <button type="button" class="btn" onclick="saveConfig()">Confirm</button>
                        </div>
                    </div>
                </div>
            </div>
            <div id="renameLabel" class="modal hide fade" tabindex="-1" role="dialog" aria-labelleby="myRenameLabel" aria-hidden="true">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                    <h3 id="myRenameLabel">ReName</h3>
                </div>
                <div class="modal-body">
                    <input type="hidden" id="oldname">
                    <input type="text" id="newName">
                </div>
                <div class="modal-footer">
                    <button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
                    <a href="#" class="btn btn-primary" id="savename" data-toggle="popover" data-placement="bottom" title data-original-title="Attention" >Save</a>

                </div>
            </div>
        </div>
    </div>


</div>
<script type="text/javascript">
    $(document).ready(function () {
        $('#myTab a').click(function (e) {
            e.preventDefault();
            $(this).tab('show');
        });
        $('#pagination li').each(
                function(){
                    if($(this).text()==$('#curpage').val()){
                        $(this).attr("class","disabled")
                    }
                }
        )

        $('#savename').click(function(e){
            newname = $('#newName').val();
            curpage = $('#curpage').val();
            oldname = $('#oldname').val();
            $.post("/rename",{newName:newname,curpage:curpage,oldname:oldname},function(data){
                if(data=="1"){
                    location.reload();
                }
                else{
                    $('#savename').attr("data-content",data);
                    $('#savename').popover();
                }
            })
        })
        if("1"==($('#curpage').val())){
            $('#Prev').parent().attr("class","disabled");
            $('#Prev').removeAttr("href");
        }
        else{
            if($('#total').val()==($('#curpage').val())){
                $('#Next').parent().attr("class","disabled");
                $('#Next').removeAttr("href");
            }
            else{
                $('#Prev').parent().removeAttr("class");
                $('#Next').parent().removeAttr("class");
                $('#Prev').attr("href","/getfile/{{curpage-1}}");
                $('#Next').attr("href","/getfile/{{curpage+1}}");
            }
        }

    })
    function getPage(_page) {
        $.post("/getfiles", {pageindex:_page}, function (data) {
            alert(data);
        })
    }
    function getFileName(data){
        $('#renameLabel').modal();
        $('#oldname').val(data);
        $('#newName').val(data);
    }
    function deleteFile(_data){
        $.post('/delete',{filename:_data},function(data){
            if(data == "1"){
                location.href='http://127.0.0.1:8080/getfile/1'
            }
        })
    }
    function saveConfig(){
        _fileLocation = $('#fileLocation').val();
        $.post('/saveConfig',{fileLocation:_fileLocation},function(data){
            if(data != "false"){
                $('#fileLocation').val(data['newLocation']);
                location.reload()
            }
        })
    }

</script>
</body>
</html>