<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="AvailableDogs.aspx.cs" Inherits="TexasRussellRescue.AvailableDogs" %>
<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
Owner Listings
</asp:Content>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
<h1 class="titleText">Owner Listings</h1>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<div style="padding-left: 50px;">
		<table>
			<tr>
				<td style="padding-bottom:50px">
					<asp:HyperLink ID="HyperLink1" CssClass="dogLink" NavigateUrl="~/RescueDogs.aspx" runat="server">Rescue Dogs</asp:HyperLink>
				</td>
			</tr>
				<tr>
				<td>
					<asp:HyperLink ID="HyperLink2" CssClass="dogLink" NavigateUrl="~/OwnerDogs.aspx" runat="server">Owner Dogs</asp:HyperLink>
				</td>
			</tr>
		</table>
	</div>
</asp:Content>
