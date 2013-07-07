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
                <form class="form-search">
                    <h2 style="margin-bottom: 10px">File Address:</h2>

                    <div class="input-append">
                        <input type="text" class="input-xxlarge" id="down_address">
                        <button type="submit" class="btn">download</button>
                    </div>
                </form>
                <table class="table table-bordered table-hover table-striped">
                    <thead>
                    <tr>
                        <td style="word-wrap: break-word" width="80%"><p class="lead text-center">File Name</p></td>
                        <td style="word-wrap: break-word" width="20%"><p class="lead text-center">Operation</p></td>
                    </tr>
                    </thead>
                    %for file in filelist:
                    <tr>
                        <td>{{file}}</td>
                        <td style="text-align: center">
                            <div class="btn-group">
                                <button class="btn">Action</button>
                                <button class="btn dropdown-toggle" data-toggle="dropdown">
                                    <span class="caret"></span>
                                </button>
                                <ul class="dropdown-menu">
                                    <li><a href="#">delete</a></li>
                                    <li><a href="javascript:$('#renameLabel').modal()" data-toggle="modal" role="button">rename</a></li>
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
                            <input type="text" placeholder="Download folder">
                            <button type="button" class="btn">Confirm</button>
                        </div>
                    </div>
                </div>
            </div>
            <div id="renameLabel" class="modal hide fade" tabindex="-1" role="dialog" aria-labelleby="myRenameLabel" aria-hidden="true">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                    <h3 id="myRenameLabel">重命名</h3>
                </div>
                <div class="modal-body">
                    <input type="text">
                </div>
                <div class="modal-footer">
                    <button class="btn" data-dismiss="modal" aria-hidden="true">关闭</button>
                    <button class="btn btn-primary">保存</button>
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
        if("1"==($('#curpage').val())){
            $('#Prev').parent().attr("class","disabled");
            $('#Prev').removeAttr("href");
        }
        else if($('#total').val()==($('#curpage').val())){
            $('#Next').parent().attr("class","disabled");
            $('#Next').removeAttr("href");
        }
        else{
            $('#Prev').parent().removeAttr("class");
            $('#Next').parent().removeAttr("class");
            $('#Prev').attr("href","/getfile/{{curpage-1}}");
            $('#Next').attr("href","/getfile/{{curpage+1}}");
        }
    })
    function getPage(_page) {
        $.post("/getfiles", {pageindex:_page}, function (data) {
            alert(data);
        })
    }

</script>
</body>
</html>