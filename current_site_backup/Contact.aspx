<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true"
	CodeBehind="Contact.aspx.cs" Inherits="TexasRussellRescue.WebForm9" %>

<%@ Register Assembly="AjaxControlToolkit" Namespace="AjaxControlToolkit" TagPrefix="asp" %>
<asp:Content ID="Content1" runat="server" ContentPlaceHolderID="HeadTitle">
	Contact Us
</asp:Content>
<asp:Content ID="PageTitle" runat="server" ContentPlaceHolderID="PageTitle">
	<h1 class="titleText">
		Contact Us</h1>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
	<div style="padding-left: 50px; padding-right: 50px;">
		<p style="padding-top: 0pt;" class="paragraph_style_1">
			Surrender your terrier in <span class="style_2">Texas</span></p><div style="float: right; padding-right:75px; padding-bottom:75px;">
			<asp:Image ID="Image3" runat="server" Width="385px" Height="435px" ImageUrl="~/myimages/Gator 2.jpg" /><asp:RoundedCornersExtender
				ID="RoundedCornersExtender3" TargetControlID="Image3" runat="server">
			</asp:RoundedCornersExtender>
		</div>
		<p class="paragraph_style_3">
			<span class="style_2">DFW</span> and <span class="style_2">North Texas</span> Contact<br />
			Adoption, Lost/Found and Shelter Contacts ONLY<br />
			<a title="mailto:froggie177@aol.com" href="mailto:froggie177@aol.com" class="style_4">froggie177@aol.com</a><br />
		</p>
		<p class="paragraph_style_3">
			Robyn G. Reed - <span class="style_2">San Antonio Area (Texas)</span><br />
			Adoption, Lost/Found and Shelter Contacts ONLY<br />
			<a title="mailto:y2alphadog@gvec.net" href="mailto:y2alphadog@gvec.net" class="style_4">
				y2alphadog@gvec.net</a><br />
		</p>
		<p class="paragraph_style_3">
			Pam Caldwell - <span class="style_2">Oklahoma</span><br />
			<a title="mailto:okcjrt@aol.com" href="mailto:okcjrt@aol.com" class="style_4">okcjrt@aol.com</a><br />
		</p>
		<p class="paragraph_style_3">
			Candace Higginbotham - <span class="style_2">Louisiana</span><br />
			<a title="mailto:candaceh@bellsouth.net" href="mailto:candaceh@bellsouth.net" class="style_4">
				candaceh@bellsouth.net</a><br />
			<br />
		</p>
		<p class="paragraph_style_3">
			For questions or concerns about this website, contact<br />
			<a title="mailto:info@texasrussellrescue.com?subject=TRR Website Inquiry" href="mailto:info@texasrussellrescue.com?subject=TRR%20Website%20Inquiry">
				Rhonda Cravey</a></p>
		<div style="float: left; padding-left:100px;">
			<asp:Image ID="Image2" runat="server" Width="365px" Height="275px" ImageUrl="~/myimages/Bohdi.jpg" /><asp:RoundedCornersExtender
				ID="RoundedCornersExtender2" TargetControlID="Image2" runat="server">
			</asp:RoundedCornersExtender>
		</div>
	</div>
</asp:Content>
