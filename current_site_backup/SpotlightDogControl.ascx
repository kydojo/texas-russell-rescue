<%@ Control Language="C#" AutoEventWireup="true" CodeBehind="SpotlightDogControl.ascx.cs" Inherits="TexasRussellRescue.SpotlightDogControl" %>
<%@ Register Assembly="AjaxControlToolkit" Namespace="AjaxControlToolkit" TagPrefix="asp" %>
<div style="padding-left:5px; width: 500px; height: 795px; -moz-border-radius: 10px; -webkit-border-radius: 10px; border-radius: 10px; border: 1px solid; background-color: #FFFF84;">
	<table>
		<tr>
			<td>
			<asp:Image ID="Image1" runat="server" Width="350px" Height="275px" ImageUrl="~/myimages/WhiskeyHose.jpg" /><asp:RoundedCornersExtender ID="RoundedCornersExtender1" TargetControlID="Image1" runat="server">
			</asp:RoundedCornersExtender>
			</td>
			<td>
				<table>
					<tr>
						<td>
							Name:
						</td>
						<td>
							<asp:Label ID="lblName" runat="server" Text="Label"></asp:Label>
						</td>
					</tr>
						<tr>
						<td>
							Location:
						</td>
						<td>
							<asp:Label ID="lblLocation" runat="server" Text="Label"></asp:Label>
						</td>
					</tr>
						<tr>
						<td>
							Sex:
						</td>
						<td>
							<asp:Label ID="lblSex" runat="server" Text="Label"></asp:Label>
						</td>
					</tr>
						<tr>
						<td>
							Age:
						</td>
						<td>
							<asp:Label ID="lblAge" runat="server" Text="Label"></asp:Label>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
	<br />
	<asp:Label ID="lblBackground" runat="server" Text=""></asp:Label>
	<br />
	<asp:Label ID="lblUpdates" runat="server" Text=""></asp:Label>
	</div><br /><br />