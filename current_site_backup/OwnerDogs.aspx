<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true"
	CodeBehind="OwnerDogs.aspx.cs" Inherits="TexasRussellRescue.OwnerDogs" %>

<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
	Owner Listings
</asp:Content>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
	<h1 class="titleText">
		Owner Listings</h1>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<div style="padding-left: 50px;padding-right: 50px;">
		<table align="center" style="text-align: center">
			<tr>
				<td>
					<p>
						All owner listings are posted per the request of an owner. The dogs listed in this
						category are not being adopted from Russell Rescue, Inc. Disclaimer: RRI is not
						responsible and/or liable for the outcome of any adoption made through these listings
						as we are only providing information. RRI is also not responsible and is held harmless
						for the accuracy and reliability of the information provided within these listings.
						Owners and adopters bear the full responsibility and liability for any dog listed.</p>
					<script language="JavaScript">
						var AAPPetScrollerSettings = {
							'searchtools_box_width': '450',
							'searchtools_box_height': '600',
							'size': '450x600_list',
							'title': '',
							'clan_name': '',
							'color': 'blue',
							'shelter_id': '77070',
							'sort_by': 'pet_name'
						};

					</script>
					<script language="JavaScript" src="http://images.adoptapet.com/js/st-portable-pet-list.js"></script>
				</td>
			</tr>
		</table>
	</div>
</asp:Content>
