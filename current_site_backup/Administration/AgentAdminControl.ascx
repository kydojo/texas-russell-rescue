<%@ Control Language="C#" AutoEventWireup="true" CodeBehind="AgentAdminControl.ascx.cs"
	Inherits="TexasRussellRescue.Administration.AgentAdminControl" %>
<%@ Register TagPrefix="telerik" Namespace="Telerik.Web.UI" Assembly="Telerik.Web.UI" %>
<table id="Table2" cellspacing="2" cellpadding="1" width="100%" border="1" rules="none"
	style="border-collapse: collapse">
	<tr class="EditFormHeader">
		<td colspan="2">
			<b>Agent</b>
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
						Name:
					</td>
					<td>
						<asp:TextBox ID="txtName" TabIndex="0" runat="server" Text='<%# DataBinder.Eval( Container, "DataItem.Name" ) %>'>
						</asp:TextBox>
					</td>
				</tr>
				
				
				<tr>
					<td>
						Background:
					</td>
					<td>
						<asp:TextBox ID="txtBackground" TabIndex="1" Text='<%# DataBinder.Eval( Container, "DataItem.Background") %>'
							runat="server" TextMode="MultiLine" Rows="5" Columns="40" >
						</asp:TextBox>
					</td>
				</tr>
				
								<tr>
					<td>
						Image:
					</td>
					<td>
						<telerik:RadUpload ID="agentImage" ControlObjectsVisibility="None"  TargetFolder="~/myimages" OverwriteExistingFiles="true" runat="server" InitialFileInputsCount="1" MaxFileInputsCount="1">
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