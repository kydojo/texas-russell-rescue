<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true"
	CodeBehind="RescueDogs.aspx.cs" Inherits="TexasRussellRescue.RescueDogs" %>

<%@ Register Assembly="Telerik.Web.UI" Namespace="Telerik.Web.UI" TagPrefix="telerik" %>
<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
	Rescue Dogs
</asp:Content>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
	<h1 class="titleText">
		Rescue Dogs</h1>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<div style="padding-left: 50px;padding-right: 50px;">
		<table align="center" style="text-align: center">
			<tr>
				<td>
					<telerik:RadPanelBar ID="RadPanelBar1" ExpandMode="SingleExpandedItem" runat="server" Width="650px" BackColor="#b0cddd">
						<Items>
							<telerik:RadPanelItem Text="Austin/San Antonio" Selected="true" Expanded="true">
								<ContentTemplate>
									<table align="center" style="text-align: center">
										<tr>
											<td>
												<script language="JavaScript">
													var AAPPetScrollerSettings = {
														'searchtools_box_width': '450',
														'searchtools_box_height': '600',
														'size': '450x600_list',
														'title': '',
														'clan_name': '',
														'color': 'blue',
														'shelter_id': '79569',
														'sort_by': 'pet_name'
													};
												</script>
												<script language="JavaScript" src="http://images.adoptapet.com/js/st-portable-pet-list.js"></script>
											</td>
										</tr>
									</table>
								</ContentTemplate>
							</telerik:RadPanelItem>
							<telerik:RadPanelItem Text="Dallas/Ft. Worth">
								<ContentTemplate>
									<table align="center" style="text-align: center">
										<tr>
											<td>
												<script language="JavaScript">
													var AAPPetScrollerSettings = {
														'searchtools_box_width': '450',
														'searchtools_box_height': '600',
														'size': '450x600_list',
														'title': '',
														'clan_name': '',
														'color': 'blue',
														'shelter_id': '79568',
														'sort_by': 'pet_name'
													};
												</script>
												<script language="JavaScript" src="http://images.adoptapet.com/js/st-portable-pet-list.js"></script>
											</td>
										</tr>
									</table>
								</ContentTemplate>
							</telerik:RadPanelItem>
							<telerik:RadPanelItem Text="Houston">
								<ContentTemplate>
									<table align="center" style="text-align: center">
										<tr>
											<td>
												<script language="JavaScript">
													var AAPPetScrollerSettings = {
														'searchtools_box_width': '450',
														'searchtools_box_height': '600',
														'size': '450x600_list',
														'title': '',
														'clan_name': '',
														'color': 'blue',
														'shelter_id': '79570',
														'sort_by': 'pet_name'
													};
												</script>
												<script language="JavaScript" src="http://images.adoptapet.com/js/st-portable-pet-list.js"></script>
											</td>
										</tr>
									</table>
								</ContentTemplate>
							</telerik:RadPanelItem>
							<telerik:RadPanelItem Text="Louisiana">
								<ContentTemplate>
									<table align="center" style="text-align: center">
										<tr>
											<td>
												<script language="JavaScript">
													var AAPPetScrollerSettings = {
														'searchtools_box_width': '450',
														'searchtools_box_height': '600',
														'size': '450x600_list',
														'title': '',
														'clan_name': '',
														'color': 'blue',
														'shelter_id': '99754',
														'sort_by': 'pet_name'
													};
												</script>
												<script language="JavaScript" src="http://images.adoptapet.com/js/st-portable-pet-list.js"></script>
											</td>
										</tr>
									</table>
								</ContentTemplate>
							</telerik:RadPanelItem>
                            <telerik:RadPanelItem Text="Oklahoma">
    							<ContentTemplate>
									<table align="center" style="text-align: center">
										<tr>
											<td>
												<script language="JavaScript">
													var AAPPetScrollerSettings = {
														'searchtools_box_width': '450',
														'searchtools_box_height': '600',
														'size': '450x600_list',
														'title': '',
														'clan_name': '',
														'color': 'blue',
														'shelter_id': '80090',
														'sort_by': 'pet_name'
													};
												</script>
												<script language="JavaScript" src="http://images.adoptapet.com/js/st-portable-pet-list.js"></script>
											</td>
										</tr>
									</table>
								</ContentTemplate>
							</telerik:RadPanelItem>
						</Items>
					</telerik:RadPanelBar>
				</td>
			</tr>
		</table>
	</div>
</asp:Content>
