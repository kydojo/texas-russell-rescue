<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Agents.aspx.cs" Inherits="TexasRussellRescue.Agents" %>
<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
Spotlight Dogs
</asp:Content>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
<h1 class="titleText">Agents</h1>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<div style="padding-left: 50px; text-align: center;">
	<table align="center" style="vertical-align: bottom">
		<tr>
			<td>
				<asp:Panel ID="Panel1" runat="server">
				</asp:Panel>
			</td>
		</tr>
	</table>
	</div>
</asp:Content>
