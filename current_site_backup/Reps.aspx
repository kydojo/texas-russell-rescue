<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Reps.aspx.cs" Inherits="TexasRussellRescue.Reps" %>
<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
Reps
</asp:Content>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
<h1 class="titleText">Reps</h1>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<div style="padding-left: 50px;">
		<p style="padding-top: 0pt;" class="Title">
			<a title="RR Adoption Release.pdf" href="Forms/RR%20Adoption%20Release.pdf">RR Adoption
				Release.pdf</a><br />
		</p>
		<p class="Title">
			<a title="RR Adoption contract.pdf" href="Forms/RR%20Adoption%20contract.pdf">RR Adoption
				contract.pdf</a><br />
		</p>
		<p style="padding-bottom: 0pt;" class="Title">
			<a title="RR Expense Report.pdf" href="Forms/RR%20Expense%20Report.pdf">RR Expense Report.pdf</a></p>
				<p style="padding-bottom: 0pt;" class="Title">
			<a title="Admin Page" href="Administration/AdminPage.aspx">Admin Page</a></p>
	</div>
</asp:Content>
