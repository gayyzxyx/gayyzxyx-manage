<!DOCTYPE html>
<html>
<head>
    <title>download page</title>
    %include head
</head>
<body>
%include head
<div class="container">
    <div class="tabbable">
        <ul class="nav nav-tabs" id="myTab">
            <li class="active"><a href="#file-download"  data-toggle="tab">File Manager</a> </li>
            <li><a href="#admin" data-toggle="tab">Admin</a> </li>
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
                        <td style="word-wrap: break-word" width="80%"><p class="lead text-center">File Name</p> </td>
                        <td style="word-wrap: break-word" width="20%"><p class="lead text-center">Operation</p> </td>
                    </tr>
                    </thead>
                    <tr>
                        <td>我们都是SB</td>
                        <td style="text-align: center"><div class="btn-group">
                            <button class="btn">Action</button>
                            <button class="btn dropdown-toggle" data-toggle="dropdown">
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu">
                                <li><a href="#">delete</a> </li>
                                <li><a href="#">rename</a> </li>
                            </ul>
                        </div> </td>
                    </tr>
                    <tr>
                        <td>我们都是SB</td>
                        <td style="text-align: center"><div class="btn-group">
                            <button class="btn">Action</button>
                            <button class="btn dropdown-toggle" data-toggle="dropdown">
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu">
                                <li><a href="#">delete</a> </li>
                                <li><a href="#">rename</a> </li>
                            </ul>
                        </div></td>
                    </tr>
                    <tr>
                        <td>我们都是SB</td>
                        <td style="text-align: center"><div class="btn-group">
                            <button class="btn">Action</button>
                            <button class="btn dropdown-toggle" data-toggle="dropdown">
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu">
                                <li><a href="#">delete</a> </li>
                                <li><a href="#">rename</a> </li>
                            </ul>
                        </div></td>
                    </tr>
                    <tr>
                        <td>我们都是SB</td>
                        <td style="text-align: center"><div class="btn-group">
                            <button class="btn">Action</button>
                            <button class="btn dropdown-toggle" data-toggle="dropdown">
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu">
                                <li><a href="#">delete</a> </li>
                                <li><a href="#">rename</a> </li>
                            </ul>
                        </div></td>
                    </tr>
                </table>
                <div class="pagination pagination-small pagination-right">
                    <ul>
                        <li class="disabled"><a href="#">Prev</a></li>
                        <li><a href="#">1</a></li>
                        <li><a href="#">2</a></li>
                        <li><a href="#">3</a></li>
                        <li><a href="#">4</a></li>
                        <li><a href="#">5</a></li>
                        <li><a href="#">Next</a></li>
                    </ul>
                </div>
            </div>
            <div class="tab-pane fade" id = "admin">
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
        </div>
    </div>


</div>
<script type="text/javascript">
    $(document).ready(function(){
        $('#myTab a').click(function (e) {
            e.preventDefault();
            $(this).tab('show');
        })
    })


</script>
</body>
</html>