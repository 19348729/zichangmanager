$(function () {
	$("#datagrid_box").datagrid({
		width:300,
		url: '/page_paiqi/',
		title: '排期档案',
		striped: true,
		singleSelect: true,
		rownumbers: true,
		columns: [[
			{
				width: 200,
				field: 'xuanzhong',
				title: '排期',
				align: 'center',
				sortable: true,
				formatter: function (value, row, index) {
					return '<a href="' + '#' + value + '" style="font-size:16px;">' + value + '</a>';
				}
			}	
		]],
		pagination: true,
		pageSize: 5,
		pageList: [5, 10, 20],
		sortName: 'xuanzhong',
		sortOrder: 'desc',
		remoteSort: true
	});

});