<%@ Control Language="C#" AutoEventWireup="true" CodeBehind="SpotlightAdminControl.ascx.cs"
	Inherits="TexasRussellRescue.Administration.SpotlightAdminControl" %>
<%@ Register TagPrefix="telerik" Namespace="Telerik.Web.UI" Assembly="Telerik.Web.UI" %>
<table id="Table2" cellspacing="2" cellpadding="1" width="100%" border="1" rules="none"
	style="border-collapse: collapse">
	<tr class="EditFormHeader">
		<td colspan="2">
			<b>Spotlight Dog</b>
		</td>
	</tr>
	<tr>
		<td>
			<table id="Table3" cellspacing="1" cellpadding="1" width="100%" border="0">
				<tr>
					<td>
					</td>
					<td>
					</td>
				</tr>
				<tr>
					<td>
						Dog Name:
					</td>
					<td>
						<asp:TextBox ID="txtDogName" runat="server" Text='<%# DataBinder.Eval( Container, "DataItem.DogName" ) %>'>
						</asp:TextBox>
					</td>
				</tr>
				<tr>
					<td>
						Location:
					</td>
					<td>
						<asp:TextBox ID="txtLocation" runat="server" Text='<%# DataBinder.Eval( Container, "DataItem.Location") %>'
							TabIndex="1">
						</asp:TextBox>
					</td>
				</tr>
				<tr>
					<td>
						Sex:
					</td>
					<td>
						<asp:TextBox ID="txtSex" runat="server" Text='<%# DataBinder.Eval( Container, "DataItem.Sex") %>'
							TabIndex="2">
						</asp:TextBox>
					</td>
				</tr>
				<tr>
					<td>
						Age:
					</td>
					<td>
						<asp:TextBox ID="txtAge" runat="server" Text='<%# DataBinder.Eval( Container, "DataItem.Age") %>'
							TabIndex="2">
						</asp:TextBox>
					</td>
				</tr>
				<tr>
					<td>
						Background:
					</td>
					<td>
						<asp:TextBox ID="txtBackground" Text='<%# DataBinder.Eval( Container, "DataItem.Background") %>'
							runat="server" TextMode="MultiLine" Rows="5" Columns="40" TabIndex="5">
						</asp:TextBox>
					</td>
				</tr>
				<tr>
					<td>
						Updates:
					</td>
					<td>
						<asp:TextBox ID="txtUpdates" Text='<%# DataBinder.Eval( Container, "DataItem.Updates") %>'
							runat="server" TextMode="MultiLine" Rows="5" Columns="40" TabIndex="5">
						</asp:TextBox>
					</td>
				</tr>
								<tr>
					<td>
						Dog Image:
					</td>
					<td>
						<telerik:RadUpload ID="dogImage" ControlObjectsVisibility="None"  TargetFolder="~/myimages" OverwriteExistingFiles="true" runat="server" InitialFileInputsCount="1" MaxFileInputsCount="1">
						</telerik:RadUpload>
					</td>
				</tr>
			</table>
</td>
<td>
</td>
</tr>
<tr>
	<td align="right" colspan="2">
		<asp:Button ID="btnUpdate" Text="Update" runat="server" CommandName="Update" Visible='<%# !(DataItem is Telerik.Web.UI.GridInsertionObject) %>'>
		</asp:Button>
		<asp:Button ID="btnInsert" Text="Insert" runat="server" CommandName="PerformInsert"
			Visible='<%# DataItem is Telerik.Web.UI.GridInsertionObject %>'></asp:Button>
		&nbsp;
		<asp:Button ID="btnCancel" Text="Cancel" runat="server" CausesValidation="False"
			CommandName="Cancel"></asp:Button>
	</td>
</tr>
</table> 