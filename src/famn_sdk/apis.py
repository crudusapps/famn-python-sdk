"""Generated asynchronous API endpoint classes."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

from .api_client import ApiClient, FileValue
from .models import *
from .models import _serialize


def _query_value(value: Any) -> str:
    value = _serialize(value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list)):
        return json.dumps(value, separators=(",", ":"))
    return str(value)


def _add_query(
    query: list[tuple[str, str]],
    name: str,
    value: Any,
    collection_format: str,
) -> None:
    if value is None:
        return
    if not isinstance(value, (list, tuple)):
        query.append((name, _query_value(value)))
        return
    if collection_format == "multi":
        query.extend((name, _query_value(item)) for item in value)
        return
    separator = {"ssv": " ", "tsv": "\t", "pipes": "|"}.get(collection_format, ",")
    query.append((name, separator.join(_query_value(item) for item in value)))


class AccountApi:
    "Account endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def change_account_language_endpoint(self, *, body: UpdateAccountLanguageRequest | None = None) -> None:
        "Change account language # Change account language"
        request_path = "/api/v1/access/account/profile/change-language"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def change_account_region_endpoint(self, *, body: UpdateAccountRegionRequest | None = None) -> None:
        "Change account region # Change account region"
        request_path = "/api/v1/access/account/profile/change-region"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def change_account_time_zone_endpoint(self, *, body: UpdateAccountTimeZoneRequest | None = None) -> None:
        "Change account time zone # Change account time zone"
        request_path = "/api/v1/access/account/profile/change-time-zone"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def confirm_delete_profile_endpoint(self, *, body: ConfirmPhoneNumberRequest | None = None) -> None:
        "Confirm delete # Confirm delete account profile request"
        request_path = "/api/v1/access/account/profile/confirm-delete"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def confirm_email_endpoint(self, *, body: ConfirmEmailRequest | None = None) -> None:
        "Confirm email # Confirm email"
        request_path = "/api/v1/access/account/email/confirm"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def confirm_phone_number_endpoint(self, *, body: ConfirmPhoneNumberRequest | None = None) -> None:
        "Confirm phone number # Confirm phone number"
        request_path = "/api/v1/access/account/phone-number/confirm"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def confirm_reset_password_request_endpoint(self, *, body: ConfirmResetPasswordRequest | None = None) -> None:
        "Confirm reset password request # Confirm reset password request"
        request_path = "/api/v1/access/account/password/confirm-reset"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=None,
        )

    async def create_app_password_endpoint(self, *, body: CreateAppPasswordRequest | None = None) -> CreateAppPasswordResponse:
        "Create app password # Create app password  Returns a new app password token (shown once), intended for CalDAV/WebDAV and similar clients."
        request_path = "/api/v1/access/account/app-passwords"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CreateAppPasswordResponse,
        )

    async def delete_profile_endpoint(self) -> None:
        "Delete account profile # Delete account profile"
        request_path = "/api/v1/access/me"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_profile_endpoint(self) -> Account:
        "Get account profile # Get account profile"
        request_path = "/api/v1/access/me"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Account,
        )

    async def list_app_passwords_endpoint(self) -> list[AppPasswordListItem]:
        "List app passwords # List app passwords  Returns app passwords for the authenticated account, without exposing raw tokens."
        request_path = "/api/v1/access/account/app-passwords"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[AppPasswordListItem],
        )

    async def register_token_endpoint(self, *, body: RegisterNotificationTokenRequestRequest | None = None) -> None:
        "Register notification token # Register notification token"
        request_path = "/api/v1/access/account/notifications/register-token"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def resend_confirm_code_endpoint(self) -> None:
        "Resend confirm code # Resend confirm code to phone number"
        request_path = "/api/v1/access/account/phone-number/resend-confirm-code"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def resend_email_confirm_code_endpoint(self) -> None:
        "Resend confirm code # Resend confirm code to email"
        request_path = "/api/v1/access/account/email/resend-confirm-code"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def reset_password_request_endpoint(self, *, body: ResetPasswordRequest | None = None) -> None:
        "Reset password request # Reset password request"
        request_path = "/api/v1/access/account/password/reset"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=None,
        )

    async def revoke_app_password_endpoint(self, id: str) -> None:
        "Revoke app password # Revoke app password  Marks an app password as revoked for the authenticated account."
        request_path = "/api/v1/access/account/app-passwords/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def unregister_token_endpoint(self) -> None:
        "Register notification token # Register notification token"
        request_path = "/api/v1/access/account/notifications/unregister-token"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def update_profile_endpoint(self, *, body: UpdateAccountRequest | None = None) -> Account:
        "Update account profile # Update account profile"
        request_path = "/api/v1/access/me"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Account,
        )

    async def upload_profile_image_endpoint(self, file: FileValue) -> Account:
        "Upload profile image # Upload profile image"
        request_path = "/api/v1/access/account/profile/upload-profile-image"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_files["file"] = file
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=Account,
        )


class AccountScoreApi:
    "AccountScore endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def get_account_score_endpoint(self, id: str) -> AccountScore:
        "Get a account score by id # Get a account score by id"
        request_path = "/api/v1/access/account/score/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=AccountScore,
        )

    async def get_account_scores_endpoint(self, *, filter: str | None = None) -> list[AccountScore]:
        "Get all account scores # Get all account scores"
        request_path = "/api/v1/access/account/score"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[AccountScore],
        )

    async def get_daily_score_endpoint(self, id: str, type: str, *, from_date: str | None = None, to_date: str | None = None) -> AccountScoreDailyResponse:
        "Get a daily score by type and id # Get a daily score by type and id"
        request_path = "/api/v1/access/account/score/daily-score"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "id", id, "")
        _add_query(request_query, "type", type, "")
        _add_query(request_query, "from_date", from_date, "")
        _add_query(request_query, "to_date", to_date, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=AccountScoreDailyResponse,
        )


class ApplicationApi:
    "Application endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_application_endpoint(self, *, body: Application | None = None) -> Application:
        "Create a new application # Create a new application"
        request_path = "/api/v1/supporting/applications/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Application,
        )

    async def delete_application_endpoint(self, application_id: str) -> None:
        "Deletes a application by id # Deletes a application by id"
        request_path = "/api/v1/supporting/applications/{application_id}"
        request_path = request_path.replace("{application_id}", quote(_query_value(application_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_application_endpoint(self, application_id: str) -> Application:
        "Get a application by id # Get a application by id"
        request_path = "/api/v1/supporting/applications/{application_id}"
        request_path = request_path.replace("{application_id}", quote(_query_value(application_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Application,
        )

    async def get_applications_endpoint(self, *, only_mine: bool | None = None) -> list[Application]:
        "Get all applications # Get all applications"
        request_path = "/api/v1/supporting/applications/"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "only_mine", only_mine, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Application],
        )

    async def update_application_endpoint(self, application_id: str, *, body: Application | None = None) -> Application:
        "Update a application by id # Update a application by id"
        request_path = "/api/v1/supporting/applications/{application_id}"
        request_path = request_path.replace("{application_id}", quote(_query_value(application_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Application,
        )


class AttachmentApi:
    "Attachment endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_attachment_endpoint(self, *, body: CreateAttachmentRequest | None = None, file: FileValue | None = None, attachmentable_id: str | None = None, attachmentable_type: str | None = None, provider: str | None = None, storage_path: str | None = None, public: bool | None = None) -> Attachment:
        "Create a new attachment # Create a new attachment"
        request_path = "/api/v1/attachments/attachments"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        if file is not None:
            request_files["file"] = file
        if attachmentable_id is not None:
            request_form["attachmentableId"] = attachmentable_id
        if attachmentable_type is not None:
            request_form["attachmentableType"] = attachmentable_type
        if provider is not None:
            request_form["provider"] = provider
        if storage_path is not None:
            request_form["storagePath"] = storage_path
        if public is not None:
            request_form["public"] = public
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=Attachment,
        )

    async def delete_attachment_endpoint(self, id: str) -> None:
        "Delete a attachment by id # Delete a attachment by id"
        request_path = "/api/v1/attachments/attachments/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_attachment_endpoint(self, id: str) -> Attachment:
        "Get a attachment by id # Get a attachment by id"
        request_path = "/api/v1/attachments/attachments/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Attachment,
        )

    async def get_attachments_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> AttachmentPaginateResponse:
        "Get all attachments # Get all attachments"
        request_path = "/api/v1/attachments/attachments"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=AttachmentPaginateResponse,
        )

    async def update_attachment_endpoint(self, id: str, *, body: Attachment | None = None) -> Attachment:
        "Update a attachment by id # Update a attachment by id"
        request_path = "/api/v1/attachments/attachments/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Attachment,
        )


class AuthenticateApi:
    "Authenticate endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def logout_endpoint(self, *, sign_out_all: bool | None = None, body: RegisterNotificationTokenRequestRequest | None = None) -> None:
        "Log user out # Log user out"
        request_path = "/api/v1/access/auth/logout"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "sign_out_all", sign_out_all, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def refresh_endpoint(self, *, body: RefreshTokenRequest | None = None) -> AuthResponse:
        "Refresh access token # Refresh access token"
        request_path = "/api/v1/access/auth/refresh"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=AuthResponse,
        )


class CalcApi:
    "Calc endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def check_compatibility_endpoint(self, body: CompatInput) -> KobleCompatResult:
        "Evaluate a car + caravan + household combination against the versioned compatibility rules. Takes a complete snapshot; returns per-rule results."
        request_path = "/api/v1/compatibility/check"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleCompatResult,
        )


class CalendarApi:
    "Calendar endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_calendar_endpoint(self, *, body: CreateCalendarRequest | None = None) -> Calendar:
        "Create a new calendar"
        request_path = "/api/v1/calendars"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Calendar,
        )

    async def create_calendar_event_endpoint(self, id: str, *, body: CreateCalendarEventRequest | None = None) -> CalendarEvent:
        "Create event for a calendar"
        request_path = "/api/v1/calendars/{id}/events"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarEvent,
        )

    async def create_calendar_permission_endpoint(self, id: str, *, body: CreateCalendarPermissionRequest | None = None) -> CalendarPermission:
        "Create permission for a calendar"
        request_path = "/api/v1/calendars/{id}/permissions"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarPermission,
        )

    async def create_remote_ics_calendar_endpoint(self, *, body: CreateRemoteICSCalendarRequest | None = None) -> Calendar:
        "Create a subscribed remote ICS calendar"
        request_path = "/api/v1/calendars/remote-ics"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Calendar,
        )

    async def delete_caldav_app_password_scope_endpoint(self, app_password_id: str) -> None:
        "Delete CalDAV app password scope"
        request_path = "/api/v1/calendars/caldav/app-password-scopes/{appPasswordId}"
        request_path = request_path.replace("{appPasswordId}", quote(_query_value(app_password_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_calendar_endpoint(self, id: str) -> None:
        "Delete a calendar by id"
        request_path = "/api/v1/calendars/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_calendar_event_endpoint(self, id: str, event_id: str) -> None:
        "Delete a calendar event by id"
        request_path = "/api/v1/calendars/{id}/events/{eventId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{eventId}", quote(_query_value(event_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_calendar_permission_endpoint(self, id: str, permission_id: str) -> None:
        "Delete permission for a calendar"
        request_path = "/api/v1/calendars/{id}/permissions/{permissionId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{permissionId}", quote(_query_value(permission_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_caldav_app_password_scopes_endpoint(self) -> list[CalDAVAppPasswordScope]:
        "List CalDAV app password scopes"
        request_path = "/api/v1/calendars/caldav/app-password-scopes"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[CalDAVAppPasswordScope],
        )

    async def get_caldav_settings_endpoint(self) -> CalDAVAccountSettings:
        "Get CalDAV account settings"
        request_path = "/api/v1/calendars/caldav/settings"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalDAVAccountSettings,
        )

    async def get_calendar_endpoint(self, id: str) -> Calendar:
        "Get a calendar by id"
        request_path = "/api/v1/calendars/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Calendar,
        )

    async def get_calendar_event_endpoint(self, id: str, event_id: str) -> CalendarEvent:
        "Get a calendar event by id"
        request_path = "/api/v1/calendars/{id}/events/{eventId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{eventId}", quote(_query_value(event_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarEvent,
        )

    async def get_calendar_events_endpoint(self, id: str, *, from_: str | None = None, to: str | None = None, expand: bool | None = None) -> list[CalendarEvent]:
        "Get events for a calendar Optionally restricted to a time range with `from`/`to` (RFC3339). With `expand=true` recurring events are replaced by their concrete occurrences within the range, honoring EXDATEs, per-occurrence exceptions, and detached instances; a range is then required."
        request_path = "/api/v1/calendars/{id}/events"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "from", from_, "")
        _add_query(request_query, "to", to, "")
        _add_query(request_query, "expand", expand, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[CalendarEvent],
        )

    async def get_calendar_notification_settings_endpoint(self, id: str) -> CalendarNotificationSetting:
        "Get notification setting for current account"
        request_path = "/api/v1/calendars/{id}/notifications"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarNotificationSetting,
        )

    async def get_calendar_permissions_endpoint(self, id: str) -> list[CalendarPermission]:
        "Get permissions for a calendar"
        request_path = "/api/v1/calendars/{id}/permissions"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[CalendarPermission],
        )

    async def get_calendars_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None) -> CalendarPaginateResponse:
        "Get all calendars"
        request_path = "/api/v1/calendars"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarPaginateResponse,
        )

    async def get_remote_ics_calendar_endpoint(self, id: str) -> CalendarExternalIntegration:
        "Get remote ICS subscription settings"
        request_path = "/api/v1/calendars/{id}/remote-ics"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarExternalIntegration,
        )

    async def sync_remote_ics_calendar_endpoint(self, id: str) -> CalendarExternalIntegration:
        "Trigger a remote ICS sync"
        request_path = "/api/v1/calendars/{id}/remote-ics/sync"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarExternalIntegration,
        )

    async def update_caldav_settings_endpoint(self, *, body: UpsertCalDAVAccountSettingsRequest | None = None) -> CalDAVAccountSettings:
        "Update CalDAV account settings"
        request_path = "/api/v1/calendars/caldav/settings"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalDAVAccountSettings,
        )

    async def update_calendar_endpoint(self, id: str, *, body: Calendar | None = None) -> Calendar:
        "Update a calendar by id"
        request_path = "/api/v1/calendars/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Calendar,
        )

    async def update_calendar_event_endpoint(self, id: str, event_id: str, *, body: CalendarEvent | None = None) -> CalendarEvent:
        "Update a calendar event by id"
        request_path = "/api/v1/calendars/{id}/events/{eventId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{eventId}", quote(_query_value(event_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarEvent,
        )

    async def update_calendar_notification_settings_endpoint(self, id: str, *, body: UpsertCalendarNotificationSettingRequest | None = None) -> CalendarNotificationSetting:
        "Update notification setting for current account"
        request_path = "/api/v1/calendars/{id}/notifications"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarNotificationSetting,
        )

    async def update_calendar_permission_endpoint(self, id: str, permission_id: str, *, body: UpdateCalendarPermissionRequest | None = None) -> CalendarPermission:
        "Update permission for a calendar"
        request_path = "/api/v1/calendars/{id}/permissions/{permissionId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{permissionId}", quote(_query_value(permission_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarPermission,
        )

    async def update_remote_ics_calendar_endpoint(self, id: str, *, body: UpdateRemoteICSCalendarRequest | None = None) -> CalendarExternalIntegration:
        "Update remote ICS subscription settings"
        request_path = "/api/v1/calendars/{id}/remote-ics"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalendarExternalIntegration,
        )

    async def upsert_caldav_app_password_scope_endpoint(self, app_password_id: str, *, body: UpsertCalDAVAppPasswordScopeRequest | None = None) -> CalDAVAppPasswordScope:
        "Upsert CalDAV app password scope"
        request_path = "/api/v1/calendars/caldav/app-password-scopes/{appPasswordId}"
        request_path = request_path.replace("{appPasswordId}", quote(_query_value(app_password_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CalDAVAppPasswordScope,
        )


class CampaignApi:
    "Campaign endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_campaign_endpoint(self, *, body: Campaign | None = None) -> Campaign:
        "Create a new campaign # Create a new campaign"
        request_path = "/api/v1/access/campaigns"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Campaign,
        )

    async def delete_campaign_endpoint(self, id: str) -> None:
        "Delete a campaign by id # Delete a campaign by id"
        request_path = "/api/v1/access/campaigns/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_campaign_endpoint(self, id: str) -> Campaign:
        "Get a campaign by id # Get a campaign by id"
        request_path = "/api/v1/access/campaigns/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Campaign,
        )

    async def get_campaigns_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> CampaignPaginateResponse:
        "Get all campaigns # Get all campaigns"
        request_path = "/api/v1/access/campaigns"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CampaignPaginateResponse,
        )

    async def update_campaign_endpoint(self, id: str, *, body: Campaign | None = None) -> Campaign:
        "Update a campaign by id # Update a campaign by id"
        request_path = "/api/v1/access/campaigns/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Campaign,
        )


class CaravansApi:
    "Caravans endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def apply_caravan_model_reference_endpoint(self, id: str, body: KobleApplyModelReferenceRequest) -> KobleCaravan:
        "Fill missing caravan fields from a selected model reference. Existing values are preserved and applied fields receive medium-confidence reference evidence."
        request_path = "/api/v1/caravans/{id}/enrich-reference"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleCaravan,
        )

    async def archive_caravan_endpoint(self, id: str) -> KobleCaravan:
        "Remove from the household: archives the object, which drops live placements elsewhere and stops future provider sync. Historical snapshots and evidence are untouched, and it can be brought back. Permanent removal is DELETE. Idempotent — archiving an archived object succeeds."
        request_path = "/api/v1/caravans/{id}/archive"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleCaravan,
        )

    async def caravan_registry_enrich_endpoint(self, id: str, *, body: KobleRegistryEnrichRequest | None = None) -> KobleCaravan:
        "Enrich an existing caravan with verified registry data (same merge policy as the vehicle endpoint)."
        request_path = "/api/v1/caravans/{id}/enrich"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleCaravan,
        )

    async def caravan_registry_lookup_endpoint(self, body: KobleRegistryLookupRequest) -> KobleImportJob:
        "Create a reviewable caravan draft from Norwegian Vegvesen, Dutch RDW or US NHTSA vPIC. countryCode defaults to NO; US vPIC is manufacturer VIN data, not a state registration record."
        request_path = "/api/v1/caravans/lookup"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleImportJob,
        )

    async def create_caravan_endpoint(self, body: CreateCaravanRequest) -> KobleCaravan:
        "Register a caravan manually; weight-critical fields get evidence rows."
        request_path = "/api/v1/caravans"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleCaravan,
        )

    async def delete_caravan_endpoint(self, id: str) -> None:
        "Soft-delete a caravan."
        request_path = "/api/v1/caravans/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_caravan_image_endpoint(self, id: str, image_id: str) -> None:
        "Remove an image from the caravan."
        request_path = "/api/v1/caravans/{id}/images/{imageId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{imageId}", quote(_query_value(image_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_caravan_endpoint(self, id: str) -> KobleCaravan:
        "Get one caravan with its equipment list."
        request_path = "/api/v1/caravans/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleCaravan,
        )

    async def list_caravan_evidence_endpoint(self, id: str) -> None:
        "List the provenance history per field."
        request_path = "/api/v1/caravans/{id}/evidence"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def list_caravan_images_endpoint(self, id: str) -> list[KobleEntityImage]:
        "List the caravan's images in gallery order."
        request_path = "/api/v1/caravans/{id}/images"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[KobleEntityImage],
        )

    async def list_caravans_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None, include_candidates: bool | None = None, collection_role: str | None = None) -> CaravanPaginateResponse:
        "List the account's caravans with filtering and pagination."
        request_path = "/api/v1/caravans"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "include_candidates", include_candidates, "")
        _add_query(request_query, "collection_role", collection_role, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CaravanPaginateResponse,
        )

    async def patch_caravan_endpoint(self, id: str, body: PatchCaravanRequest) -> KobleCaravan:
        "Patch caravan fields; corrections are recorded as user-override evidence."
        request_path = "/api/v1/caravans/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleCaravan,
        )

    async def set_caravan_scope_endpoint(self, id: str, body: KobleMoveScopeRequest) -> KobleCaravan:
        "Share, transfer or unshare a caravan. spaceId set moves it into that space (needs koble.create there); spaceId null makes it private (needs koble.manage_sharing in its current space)."
        request_path = "/api/v1/caravans/{id}/scope"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleCaravan,
        )

    async def upload_caravan_image_endpoint(self, id: str, file: FileValue, *, alt_text: str | None = None) -> KobleEntityImage:
        "Upload an image (multipart field \"file\", optional \"altText\") and attach it to the caravan."
        request_path = "/api/v1/caravans/{id}/images"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_files["file"] = file
        if alt_text is not None:
            request_form["altText"] = alt_text
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=KobleEntityImage,
        )


class ChangelogApi:
    "Changelog endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_changelog_endpoint(self) -> ApplicationChangelog:
        "Create a new changelog entry # Create a new changelog entry"
        request_path = "/api/v1/supporting/changelogs/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ApplicationChangelog,
        )

    async def delete_changelog_endpoint(self) -> None:
        "Deletes a changelog entry by id # Deletes a changelog entry by id"
        request_path = "/api/v1/supporting/changelogs/{changelog_id}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_changelog_endpoint(self) -> ApplicationChangelog:
        "Get a changelog entry by id # Get a changelog entry by id"
        request_path = "/api/v1/supporting/changelogs/{changelog_id}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=ApplicationChangelog,
        )

    async def get_changelogs_endpoint(self) -> list[ApplicationChangelog]:
        "Get all changelog entries # Get all changelog entries"
        request_path = "/api/v1/supporting/changelogs/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=list[ApplicationChangelog],
        )

    async def update_changelog_endpoint(self) -> ApplicationChangelog:
        "Update a changelog entry by id # Update a changelog entry by id"
        request_path = "/api/v1/supporting/changelogs/{changelog_id}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ApplicationChangelog,
        )


class ChatApi:
    "Chat endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_chat_endpoint(self, *, body: CreateChatRequest | None = None) -> Chat:
        "Create a new chat # Create a new chat"
        request_path = "/api/v1/chats"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Chat,
        )

    async def create_chat_message_endpoint(self, chat_id: str, *, body: CreateChatMessageRequest | None = None) -> ChatMessage:
        "Create a new chat message # Create a new chat message"
        request_path = "/api/v1/chats/{chat_id}/messages"
        request_path = request_path.replace("{chat_id}", quote(_query_value(chat_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ChatMessage,
        )

    async def delete_chat_endpoint(self, id: str) -> None:
        "Delete a chat by id # Delete a chat by id"
        request_path = "/api/v1/chats/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_chat_message_endpoint(self, chat_id: str, id: str) -> None:
        "Delete a chat message by id # Delete a chat message by id"
        request_path = "/api/v1/chats/{chat_id}/messages/{id}"
        request_path = request_path.replace("{chat_id}", quote(_query_value(chat_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def find_all_contacts_endpoint(self, *, search: str | None = None) -> list[User]:
        "Get all user contacts # Get all user contacts"
        request_path = "/api/v1/chats/contacts"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "search", search, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[User],
        )

    async def get_chat_endpoint(self, id: str) -> Chat:
        "Get a chat by id # Get a chat by id"
        request_path = "/api/v1/chats/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Chat,
        )

    async def get_chat_message_endpoint(self, chat_id: str, id: str) -> ChatMessage:
        "Get a chat message by id # Get a chat message by id"
        request_path = "/api/v1/chats/{chat_id}/messages/{id}"
        request_path = request_path.replace("{chat_id}", quote(_query_value(chat_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ChatMessage,
        )

    async def get_chat_messages_endpoint(self, chat_id: str, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> ChatMessagePaginateResponse:
        "Get all chat messages # Get all chat messages"
        request_path = "/api/v1/chats/{chat_id}/messages"
        request_path = request_path.replace("{chat_id}", quote(_query_value(chat_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ChatMessagePaginateResponse,
        )

    async def get_chats_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> ChatPaginateResponse:
        "Get all chats # Get all chats"
        request_path = "/api/v1/chats"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ChatPaginateResponse,
        )

    async def get_users_from_chats_endpoint(self) -> list[User]:
        "Get users from chats # Get users from chats"
        request_path = "/api/v1/chats/users"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[User],
        )

    async def update_chat_endpoint(self, id: str, *, body: Chat | None = None) -> Chat:
        "Update a chat by id # Update a chat by id"
        request_path = "/api/v1/chats/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Chat,
        )

    async def update_chat_message_endpoint(self, chat_id: str, id: str, *, body: ChatMessage | None = None) -> ChatMessage:
        "Update a chat message by id # Update a chat message by id"
        request_path = "/api/v1/chats/{chat_id}/messages/{id}"
        request_path = request_path.replace("{chat_id}", quote(_query_value(chat_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ChatMessage,
        )


class ClubCardApi:
    "ClubCard endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_club_card_endpoint(self, *, body: CreateClubCardRequest | None = None, file: FileValue | None = None, name: str | None = None, valid_from: str | None = None, valid_to: str | None = None, chain_id: str | None = None, space_id: str | None = None, shareable: bool | None = None) -> ClubCard:
        "Create a new club card # Create a new club card"
        request_path = "/api/v1/shopping/club-cards"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        if file is not None:
            request_files["file"] = file
        if name is not None:
            request_form["name"] = name
        if valid_from is not None:
            request_form["validFrom"] = valid_from
        if valid_to is not None:
            request_form["validTo"] = valid_to
        if chain_id is not None:
            request_form["chainId"] = chain_id
        if space_id is not None:
            request_form["spaceId"] = space_id
        if shareable is not None:
            request_form["shareable"] = shareable
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=ClubCard,
        )

    async def delete_club_card_endpoint(self, id: str) -> None:
        "Delete a club card by id # Delete a club card by id"
        request_path = "/api/v1/shopping/club-cards/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_club_card_endpoint(self, id: str) -> ClubCard:
        "Get a club card by id # Get a club card by id"
        request_path = "/api/v1/shopping/club-cards/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ClubCard,
        )

    async def get_club_card_image_endpoint(self, id: str) -> list[int]:
        "Get a club card image by id # Get a club card image by id"
        request_path = "/api/v1/shopping/club-cards/{id}/image"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[int],
        )

    async def get_club_card_store_chains_endpoint(self) -> list[ClubCardStoreChain]:
        "Get club card store chains # Get club card store chains"
        request_path = "/api/v1/shopping/club-cards/chains"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[ClubCardStoreChain],
        )

    async def get_club_cards_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None) -> ClubCardPaginateResponse:
        "Get all club cards # Get all club cards"
        request_path = "/api/v1/shopping/club-cards"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "spaceId", space_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ClubCardPaginateResponse,
        )

    async def update_club_card_endpoint(self, id: str, *, body: ClubCard | None = None) -> ClubCard:
        "Update a club card by id # Update a club card by id"
        request_path = "/api/v1/shopping/club-cards/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ClubCard,
        )


class ContactApi:
    "Contact endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_contact_endpoint(self, *, body: CreateContactRequest | None = None) -> Contact:
        "Create contact"
        request_path = "/api/v1/contacts"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Contact,
        )

    async def delete_contact_endpoint(self, id: str) -> None:
        "Delete contact by ID"
        request_path = "/api/v1/contacts/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_contact_endpoint(self, id: str) -> Contact:
        "Get contact by ID"
        request_path = "/api/v1/contacts/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Contact,
        )

    async def get_contacts_endpoint(self, *, space_id: str | None = None, q: str | None = None) -> list[Contact]:
        "Get contacts"
        request_path = "/api/v1/contacts"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "spaceId", space_id, "")
        _add_query(request_query, "q", q, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Contact],
        )

    async def patch_contact_endpoint(self, id: str, *, body: PatchContactRequest | None = None) -> Contact:
        "Patch contact by ID"
        request_path = "/api/v1/contacts/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Contact,
        )


class CookbookApi:
    "Cookbook endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def calculate_product_amount_endpoint(self, *, body: RecipeIngredient | None = None) -> RecipeIngredientCalculateProductAmountResult:
        "Calculate product amount for a recipe ingredient # Calculate product amount for a recipe ingredient"
        request_path = "/api/v1/cookbooks/recipe-ingredients/calculate-product-amount"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipeIngredientCalculateProductAmountResult,
        )

    async def create_cookbook_endpoint(self, *, body: CreateCookbookRequest | None = None) -> Cookbook:
        "Create a new cookbook # Create a new cookbook"
        request_path = "/api/v1/cookbooks"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Cookbook,
        )

    async def create_ingredient_endpoint(self, *, body: Ingredient | None = None) -> Ingredient:
        "Create a new ingredient # Create a new ingredient"
        request_path = "/api/v1/cookbooks/ingredients"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Ingredient,
        )

    async def create_ingredient_product_preference_endpoint(self) -> IngredientProductPreference:
        "Create an ingredient product preference"
        request_path = "/api/v1/cookbooks/ingredient-product-preferences"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=IngredientProductPreference,
        )

    async def create_recipe_endpoint(self, cookbook_id: str, *, body: CreateRecipeRequest | None = None) -> Recipe:
        "Create a new recipe # Create a new recipe"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Recipe,
        )

    async def delete_cookbook_endpoint(self, id: str) -> None:
        "Delete a cookbook by id # Delete a cookbook by id"
        request_path = "/api/v1/cookbooks/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_ingredient_endpoint(self, id: str) -> None:
        "Delete a ingredient by id # Delete a ingredient by id"
        request_path = "/api/v1/cookbooks/ingredients/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_ingredient_product_preference_endpoint(self) -> None:
        "Delete an ingredient product preference"
        request_path = "/api/v1/cookbooks/ingredient-product-preferences/{id}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_recipe_endpoint(self, cookbook_id: str, id: str) -> None:
        "Delete a recipe by id # Delete a recipe by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_recipe_ingredient_endpoint(self, cookbook_id: str, id: str, ingredient_id: str) -> None:
        "Delete a recipe ingredient by id # Delete a recipe ingredient by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}/ingredients/{ingredient_id}"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{ingredient_id}", quote(_query_value(ingredient_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_recipe_instruction_endpoint(self, cookbook_id: str, id: str, instruction_id: str) -> None:
        "Delete a recipe instruction by id # Delete a recipe instruction by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}/instructions/{instruction_id}"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{instruction_id}", quote(_query_value(instruction_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def favorite_cookbook_endpoint(self, id: str) -> CookbookUserLink:
        "Mark cookbook as favorite # Mark cookbook as favorite"
        request_path = "/api/v1/cookbooks/{id}/favorite"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CookbookUserLink,
        )

    async def favorite_recipe_endpoint(self, cookbook_id: str, id: str) -> RecipeFavorite:
        "Mark recipe as favorite # Mark recipe as favorite"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}/favorite"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipeFavorite,
        )

    async def get_all_recipes_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None, query: str | None = None) -> RecipePaginateResponse:
        "Get all recipes from all cookbooks # Get all recipes from all cookbooks"
        request_path = "/api/v1/cookbooks/recipes"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "query", query, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipePaginateResponse,
        )

    async def get_cookbook_endpoint(self, id: str) -> Cookbook:
        "Get a cookbook by id # Get a cookbook by id"
        request_path = "/api/v1/cookbooks/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Cookbook,
        )

    async def get_cookbooks_endpoint(self, *, space_id: str | None = None) -> list[Cookbook]:
        "Get all cookbooks # Get all cookbooks"
        request_path = "/api/v1/cookbooks"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Cookbook],
        )

    async def get_cookbooks_endpoint_v2(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None) -> CookbookPaginateResponse:
        "Get all cookbooks # Get all cookbooks"
        request_path = "/api/v2/cookbooks"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CookbookPaginateResponse,
        )

    async def get_favorite_recipe_endpoint(self, cookbook_id: str, id: str) -> RecipeFavorite:
        "Get recipe favorite status # Get recipe favorite status"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}/favorite"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipeFavorite,
        )

    async def get_ingredient_endpoint(self, id: str) -> Ingredient:
        "Get a ingredient by id # Get a ingredient by id"
        request_path = "/api/v1/cookbooks/ingredients/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Ingredient,
        )

    async def get_ingredient_product_preference_endpoint(self) -> IngredientProductPreference:
        "Get an ingredient product preference"
        request_path = "/api/v1/cookbooks/ingredient-product-preferences/{id}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=IngredientProductPreference,
        )

    async def get_ingredient_product_preferences_endpoint(self) -> IngredientProductPreferencePaginateResponse:
        "Get ingredient product preferences"
        request_path = "/api/v1/cookbooks/ingredient-product-preferences"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=IngredientProductPreferencePaginateResponse,
        )

    async def get_ingredients_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> IngredientPaginateResponse:
        "Get all ingredients # Get all ingredients"
        request_path = "/api/v1/cookbooks/ingredients"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=IngredientPaginateResponse,
        )

    async def get_recipe_cost_endpoint(self, cookbook_id: str, id: str, *, yield_: int | None = None) -> RecipeCost:
        "Get a recipe cost by id # Get a recipe cost by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}/cost"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "yield", yield_, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipeCost,
        )

    async def get_recipe_endpoint(self, cookbook_id: str, id: str) -> Recipe:
        "Get a recipe by id # Get a recipe by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Recipe,
        )

    async def get_recipe_nutrition_endpoint(self, cookbook_id: str, id: str, *, yield_: int | None = None) -> RecipeNutrition:
        "Get recipe nutritional contents by id # Get recipe nutritional contents by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}/nutrition"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "yield", yield_, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipeNutrition,
        )

    async def get_recipes_endpoint(self, cookbook_id: str) -> list[Recipe]:
        "Get all recipes # Get all recipes"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Recipe],
        )

    async def get_recipes_v2_endpoint(self, cookbook_id: str, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, query: str | None = None) -> RecipePaginateResponse:
        "Get all recipes # Get all recipes"
        request_path = "/api/v2/cookbooks/{cookbook_id}/recipes"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "query", query, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipePaginateResponse,
        )

    async def import_recipe_endpoint(self, cookbook_id: str, *, body: RecipeImportRequest | None = None) -> Recipe:
        "Import a recipe # Import a recipe"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/import"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Recipe,
        )

    async def patch_ingredient_product_preference_endpoint(self) -> IngredientProductPreference:
        "Patch an ingredient product preference"
        request_path = "/api/v1/cookbooks/ingredient-product-preferences/{id}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=IngredientProductPreference,
        )

    async def remove_vote_recipe_endpoint(self, cookbook_id: str, id: str) -> RecipeVote:
        "Remove vote on a recipe by id # Remove vote on a recipe by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}/vote"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipeVote,
        )

    async def unfavorite_cookbook_endpoint(self, id: str) -> CookbookUserLink:
        "Remove cookbook from favorites # Remove cookbook from favorites"
        request_path = "/api/v1/cookbooks/{id}/favorite"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CookbookUserLink,
        )

    async def unfavorite_recipe_endpoint(self, cookbook_id: str, id: str) -> RecipeFavorite:
        "Unmark recipe as favorite # Unmark recipe as favorite"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}/favorite"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipeFavorite,
        )

    async def update_cookbook_endpoint(self, id: str, *, body: Cookbook | None = None) -> Cookbook:
        "Update a cookbook by id # Update a cookbook by id"
        request_path = "/api/v1/cookbooks/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Cookbook,
        )

    async def update_ingredient_endpoint(self, id: str, *, body: Ingredient | None = None) -> Ingredient:
        "Update a ingredient by id # Update a ingredient by id"
        request_path = "/api/v1/cookbooks/ingredients/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Ingredient,
        )

    async def update_recipe_endpoint(self, cookbook_id: str, id: str, *, body: Recipe | None = None) -> Recipe:
        "Update a recipe by id # Update a recipe by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Recipe,
        )

    async def upload_image_recipe_endpoint(self, cookbook_id: str, recipe_id: str, file: FileValue) -> Recipe:
        "Upload image to a recipe by id # Upload image to a recipe by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{recipe_id}/upload-image"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{recipe_id}", quote(_query_value(recipe_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_files["file"] = file
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=Recipe,
        )

    async def upload_scan_recipe_image_endpoint(self, cookbook_id: str, file: FileValue) -> RecipeImageScanRequest:
        "Uploads a recipe import image # Uploads a recipe import image"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/import/upload-image"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_files["file"] = file
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=RecipeImageScanRequest,
        )

    async def vote_recipe_endpoint(self, cookbook_id: str, id: str, *, body: RecipeVoteRequest | None = None) -> RecipeVote:
        "Vote on a recipe by id # Vote on a recipe by id"
        request_path = "/api/v1/cookbooks/{cookbook_id}/recipes/{id}/vote"
        request_path = request_path.replace("{cookbook_id}", quote(_query_value(cookbook_id), safe=""))
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RecipeVote,
        )


class DeviceApi:
    "Device endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def confirm_device_pairing_endpoint(self, *, body: ConfirmDevicePairingRequest | None = None) -> ConfirmDevicePairingResponse:
        "Confirm pairing and bind the device to a user-owned relation"
        request_path = "/api/v1/access/devices/pair/confirm"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ConfirmDevicePairingResponse,
        )

    async def create_device_endpoint(self, *, body: CreateDeviceRequest | None = None) -> Device:
        "Create a new device # Create a new device"
        request_path = "/api/v1/access/devices"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Device,
        )

    async def delete_device_endpoint(self, id: str) -> None:
        "Delete a device by id # Delete a device by id"
        request_path = "/api/v1/access/devices/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_current_device_endpoint(self) -> DeviceTokenDeviceResponse:
        "Get device info for the current device token"
        request_path = "/api/v1/access/devices/me"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=DeviceTokenDeviceResponse,
        )

    async def get_device_endpoint(self, id: str) -> Device:
        "Get a device by id # Get a device by id"
        request_path = "/api/v1/access/devices/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Device,
        )

    async def get_devices_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> DevicePaginateResponse:
        "Get all devices # Get all devices"
        request_path = "/api/v1/access/devices"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=DevicePaginateResponse,
        )

    async def poll_device_pairing_endpoint(self, *, body: PollDevicePairingRequest | None = None) -> DeviceTokenResponse:
        "Poll pairing status and get device tokens when approved"
        request_path = "/api/v1/access/devices/pair/poll"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=DeviceTokenResponse,
        )

    async def rotate_device_refresh_token_endpoint(self, *, body: DeviceTokenRefreshRequest | None = None) -> DeviceTokenResponse:
        "Rotate a device refresh token and issue a fresh access+refresh token pair"
        request_path = "/api/v1/access/devices/token"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=DeviceTokenResponse,
        )

    async def start_device_pairing_endpoint(self, *, body: StartDevicePairingRequest | None = None) -> StartDevicePairingResponse:
        "Start a short-lived device pairing session"
        request_path = "/api/v1/access/devices/pair/start"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StartDevicePairingResponse,
        )

    async def update_device_endpoint(self, id: str, *, body: Device | None = None) -> Device:
        "Update a device by id # Update a device by id"
        request_path = "/api/v1/access/devices/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Device,
        )


class EntryApi:
    "Entry endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_entry_endpoint(self, *, app_name: str | None = None, application: str | None = None, body: CreateEntryRequest | None = None) -> EntryResponse:
        "Create a new entry for admin/editor. # Create a new entry for admin/editor"
        request_path = "/api/v1/supporting/entries"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=EntryResponse,
        )

    async def delete_entry_endpoint(self, id: str, *, app_name: str | None = None, application: str | None = None) -> None:
        "Delete an entry. # Delete an entry"
        request_path = "/api/v1/supporting/entries/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_entries_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, app_name: str | None = None, application: str | None = None, type: str | None = None, status: str | None = None, key: str | None = None) -> EntryPaginateResponse:
        "Get all entries for admin/editor. # Get all entries for admin/editor"
        request_path = "/api/v1/supporting/entries"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        _add_query(request_query, "type", type, "")
        _add_query(request_query, "status", status, "")
        _add_query(request_query, "key", key, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=EntryPaginateResponse,
        )

    async def get_entry_endpoint(self, id: str, *, app_name: str | None = None, application: str | None = None) -> EntryResponse:
        "Get one entry for admin/editor. # Get one entry for admin/editor"
        request_path = "/api/v1/supporting/entries/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=EntryResponse,
        )

    async def get_entry_types_endpoint(self) -> EntryTypeOptionListResponse:
        "Get entry type options. # Get entry type options"
        request_path = "/api/v1/supporting/entries/types"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=EntryTypeOptionListResponse,
        )

    async def get_help_entry_endpoint(self, key: str, *, app_name: str | None = None, application: str | None = None, locale: str | None = None, lang: str | None = None) -> LocalizedEntry:
        "Resolve published help content by key (Flutter clients). # Resolve published help content by key"
        request_path = "/api/v1/supporting/entries/help/{key}"
        request_path = request_path.replace("{key}", quote(_query_value(key), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        _add_query(request_query, "locale", locale, "")
        _add_query(request_query, "lang", lang, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=LocalizedEntry,
        )

    async def get_help_segment_endpoint(self, key: str, segment_key: str, *, app_name: str | None = None, application: str | None = None, locale: str | None = None, lang: str | None = None) -> LocalizedSegment:
        "Resolve one help segment by key (Flutter contextual help). # Resolve one help segment by key"
        request_path = "/api/v1/supporting/entries/help/{key}/segments/{segmentKey}"
        request_path = request_path.replace("{key}", quote(_query_value(key), safe=""))
        request_path = request_path.replace("{segmentKey}", quote(_query_value(segment_key), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        _add_query(request_query, "locale", locale, "")
        _add_query(request_query, "lang", lang, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=LocalizedSegment,
        )

    async def get_published_entries_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, app_name: str | None = None, application: str | None = None, locale: str | None = None, lang: str | None = None, type: str | None = None, types: str | None = None) -> LocalizedEntryPaginateResponse:
        "List published content (Astro/web clients). # List published content for Astro/web clients"
        request_path = "/api/v1/supporting/entries/published"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        _add_query(request_query, "locale", locale, "")
        _add_query(request_query, "lang", lang, "")
        _add_query(request_query, "type", type, "")
        _add_query(request_query, "types", types, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=LocalizedEntryPaginateResponse,
        )

    async def get_published_entry_by_key_endpoint(self, key: str, *, app_name: str | None = None, application: str | None = None, locale: str | None = None, lang: str | None = None, type: str | None = None, types: str | None = None) -> LocalizedEntryResponse:
        "Resolve a published entry by key (web/app clients). # Resolve a published entry by key"
        request_path = "/api/v1/supporting/entries/published/by-key/{key}"
        request_path = request_path.replace("{key}", quote(_query_value(key), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        _add_query(request_query, "locale", locale, "")
        _add_query(request_query, "lang", lang, "")
        _add_query(request_query, "type", type, "")
        _add_query(request_query, "types", types, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=LocalizedEntryResponse,
        )

    async def get_published_entry_by_slug_endpoint(self, *, app_name: str | None = None, application: str | None = None, locale: str | None = None, lang: str | None = None, type: str | None = None, types: str | None = None, slug: str | None = None) -> LocalizedEntryResponse:
        "Resolve a published entry by localized slug (Astro/web clients). # Resolve a published entry by localized slug"
        request_path = "/api/v1/supporting/entries/published/by-slug"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        _add_query(request_query, "locale", locale, "")
        _add_query(request_query, "lang", lang, "")
        _add_query(request_query, "type", type, "")
        _add_query(request_query, "types", types, "")
        _add_query(request_query, "slug", slug, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=LocalizedEntryResponse,
        )

    async def update_entry_endpoint(self, id: str, *, app_name: str | None = None, application: str | None = None, body: CreateEntryRequest | None = None) -> EntryResponse:
        "Update an entry for admin/editor. # Update an entry for admin/editor"
        request_path = "/api/v1/supporting/entries/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "application", application, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=EntryResponse,
        )


class FAQApi:
    "FAQ endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_faq_endpoint(self, *, body: FAQ | None = None) -> FAQ:
        "Create a new faq # Create a new faq"
        request_path = "/api/v1/supporting/faqs/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FAQ,
        )

    async def delete_faq_endpoint(self, faq_id: str) -> None:
        "Deletes a faq by id # Deletes a faq by id"
        request_path = "/api/v1/supporting/faqs/{faq_id}"
        request_path = request_path.replace("{faq_id}", quote(_query_value(faq_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_faq_endpoint(self, faq_id: str) -> FAQ:
        "Get a faq by id # Get a faq by id"
        request_path = "/api/v1/supporting/faqs/{faq_id}"
        request_path = request_path.replace("{faq_id}", quote(_query_value(faq_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FAQ,
        )

    async def get_faqs_endpoint(self, *, app_name: str | None = None) -> list[FAQ]:
        "Get all faqs # Get all faqs"
        request_path = "/api/v1/supporting/faqs/"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=list[FAQ],
        )

    async def update_faq_endpoint(self, faq_id: str, *, body: FAQ | None = None) -> FAQ:
        "Update a faq by id # Update a faq by id"
        request_path = "/api/v1/supporting/faqs/{faq_id}"
        request_path = request_path.replace("{faq_id}", quote(_query_value(faq_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FAQ,
        )


class FeatureApi:
    "Feature endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_feature_endpoint(self, *, body: Feature | None = None) -> Feature:
        "Create a new feature # Create a new feature"
        request_path = "/api/v1/supporting/features/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Feature,
        )

    async def create_feature_rule_endpoint(self, feature_id: str, *, body: FeatureRule | None = None) -> FeatureRule:
        "Create a new feature rule # Create a new feature rule"
        request_path = "/api/v1/supporting/features/{feature_id}"
        request_path = request_path.replace("{feature_id}", quote(_query_value(feature_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FeatureRule,
        )

    async def delete_feature_endpoint(self, feature_id: str) -> None:
        "Deletes a feature by id # Deletes a feature by id"
        request_path = "/api/v1/supporting/features/{feature_id}"
        request_path = request_path.replace("{feature_id}", quote(_query_value(feature_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_feature_endpoint(self, feature_id: str) -> Feature:
        "Get a feature by id # Get a feature by id"
        request_path = "/api/v1/supporting/features/{feature_id}"
        request_path = request_path.replace("{feature_id}", quote(_query_value(feature_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Feature,
        )

    async def get_features_endpoint(self, *, platform: str | None = None, version: str | None = None) -> list[Feature]:
        "Get all features # Get all features"
        request_path = "/api/v1/supporting/features/"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "platform", platform, "")
        _add_query(request_query, "version", version, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Feature],
        )

    async def update_feature_endpoint(self, feature_id: str, *, body: Feature | None = None) -> Feature:
        "Update a feature by id # Update a feature by id"
        request_path = "/api/v1/supporting/features/{feature_id}"
        request_path = request_path.replace("{feature_id}", quote(_query_value(feature_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Feature,
        )


class FileApi:
    "File endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def delete_file_endpoint(self, id: str) -> None:
        "Delete a file by id # Delete a file by id"
        request_path = "/api/v1/files/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_document_categories_endpoint(self) -> list[DocCategory]:
        "Get document categories # Get document categories"
        request_path = "/api/v1/files/doc-categories"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[DocCategory],
        )

    async def get_download_url_endpoint(self, id: str) -> FileDownloadResponse:
        "Create a presigned download URL # Create a presigned download URL"
        request_path = "/api/v1/files/download/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FileDownloadResponse,
        )

    async def get_file_endpoint(self, id: str) -> FileModel:
        "Get a file by id # Get a file by id"
        request_path = "/api/v1/files/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FileModel,
        )

    async def get_files_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, query: str | None = None) -> FilePaginateResponse:
        "Get all files # Get all files"
        request_path = "/api/v1/files"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "query", query, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FilePaginateResponse,
        )

    async def post_upload_complete_endpoint(self, *, body: CompleteUploadRequest | None = None) -> FileModel:
        "Complete an upload reservation # Complete an upload reservation"
        request_path = "/api/v1/files/upload-complete"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FileModel,
        )

    async def post_upload_endpoint(self, *, body: CreateUploadRequest | None = None) -> CreateUploadResponse:
        "Create a presigned upload URL # Create a presigned upload URL"
        request_path = "/api/v1/files/upload"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CreateUploadResponse,
        )

    async def post_upload_multipart_complete_endpoint(self, *, body: MultipartPartCompleteRequest | None = None) -> FileModel:
        "Complete a multipart upload # Complete a multipart upload"
        request_path = "/api/v1/files/upload-multipart-complete"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FileModel,
        )

    async def post_upload_multipart_endpoint(self, *, body: CreateUploadRequest | None = None) -> CreateUploadResponse:
        "Initiate a multipart upload # Initiate a multipart upload"
        request_path = "/api/v1/files/upload-multipart"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CreateUploadResponse,
        )

    async def post_upload_multipart_part_endpoint(self, *, body: MultipartPartURLRequest | None = None) -> CreateUploadResponse:
        "Create a presigned URL for a multipart upload part # Create a presigned URL for a multipart upload part"
        request_path = "/api/v1/files/upload-multipart-part"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=CreateUploadResponse,
        )

    async def relation_summaries_endpoint(self, *, body: RelationSummaryRequest | None = None) -> RelationSummaryResponse:
        "Count documents per relation # Count the documents attached to each of a set of relations  Answers \"which of these items have a photo, a receipt, nothing\" in one call. The per-relation file list would need one request per item, which is what a property-wide or space-wide report cannot afford.  Every requested relationId comes back, including ones with no documents and ones the caller may not read. Those are deliberately indistinguishable: a differentiated answer would let a caller probe for the existence of another household's item."
        request_path = "/api/v1/files/relation-summaries"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RelationSummaryResponse,
        )

    async def search_files_endpoint(self) -> list[FileModel]:
        "Search files # Search files"
        request_path = "/api/v1/files/search"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[FileModel],
        )

    async def update_file_endpoint(self, id: str, *, body: FileModel | None = None) -> FileModel:
        "Update a file by id # Update a file by id"
        request_path = "/api/v1/files/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=FileModel,
        )


class HoldingsApi:
    "Holdings endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_holding_item_endpoint(self, *, body: CreateHoldingItemRequest | None = None) -> HoldingItem:
        "Create a household item # Create a household item  The item's space is taken from the property it is created in, so it cannot be placed into a space independently of its property."
        request_path = "/api/v1/holdings/items"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=HoldingItem,
        )

    async def create_insurance_export_endpoint(self, id: str, *, body: CreateInsuranceExportRequest | None = None) -> InsuranceExportReport:
        "Export an insurance snapshot # Render a snapshot into a structured report  Totals per room and per category, every item, and references to the archived evidence. Only a ready snapshot can be exported; one still being assembled is refused with 409, because a report of an incomplete inventory that looks complete is the one thing this must never produce.  The report is generated rather than stored. It is a pure function of the snapshot and the template version, both immutable, so it regenerates identically — and nothing stored means no stale copy to expire or leak."
        request_path = "/api/v1/holdings/insurance-snapshots/{id}/exports"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=InsuranceExportReport,
        )

    async def create_insurance_snapshot_endpoint(self, idempotency_key: str, *, body: CreateInsuranceSnapshotRequest | None = None) -> InsuranceSnapshot:
        "Capture an insurance snapshot # Capture immutable proof of what a space or property contains  Requires an Idempotency-Key header. Capture copies every document to immutable storage and is slow enough that clients retry it; a retry with the same key returns the snapshot the first call made rather than archiving everything a second time.  The snapshot supersedes whatever was current for the same scope, which starts that snapshot's retention. Capture fails rather than producing a snapshot missing evidence it believes it has."
        request_path = "/api/v1/holdings/insurance-snapshots"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_headers["Idempotency-Key"] = _query_value(idempotency_key)
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=InsuranceSnapshot,
        )

    async def create_valuation_record_endpoint(self, *, body: CreateValuationRecordRequest | None = None) -> ValuationRecord:
        "File a valuation # File a valuation against a property or an item  The space is taken from the subject, so a valuation cannot be filed into a space the caller named independently of the thing being valued. subjectType external_ref is reserved and rejected with 400: it has no owning property to authorize against."
        request_path = "/api/v1/holdings/valuations"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ValuationRecord,
        )

    async def delete_holding_item_endpoint(self, id: str) -> None:
        "Delete a household item by id # Delete a household item by id  Soft delete: the item stops appearing but is retained, because it may be part of an insurance snapshot."
        request_path = "/api/v1/holdings/items/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_insurance_snapshot_endpoint(self, id: str) -> None:
        "Delete an insurance snapshot # Delete an insurance snapshot  Soft delete. The frozen rows and the archived evidence survive a grace period before anything is purged, because deleting the only proof of what you own is a mistake worth being able to undo."
        request_path = "/api/v1/holdings/insurance-snapshots/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def download_insurance_export_endpoint(self, id: str, export_id: str) -> ArchiveDownloadResponse:
        "Download a rendered report # Get a temporary link to a rendered report  Answers 409 while the report is still rendering or if it failed, rather than a link that will not resolve. The link is short-lived and the artifact lives under the snapshot, so it disappears when the snapshot does."
        request_path = "/api/v1/holdings/insurance-snapshots/{id}/exports/{exportId}/download"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{exportId}", quote(_query_value(export_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ArchiveDownloadResponse,
        )

    async def get_current_valuation_record_endpoint(self, subject_type: str, subject_id: str, *, as_of: str | None = None) -> ValuationRecord:
        "Get the current value of one subject # Get the record that represents a subject's value  Applies the same selection rule an insurance snapshot uses: the most recent record dated at or before as_of, breaking ties on the strength of the basis. Responds 204 when the subject has never been valued."
        request_path = "/api/v1/holdings/valuations/current"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "subject_type", subject_type, "")
        _add_query(request_query, "subject_id", subject_id, "")
        _add_query(request_query, "as_of", as_of, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ValuationRecord,
        )

    async def get_holding_item_endpoint(self, id: str) -> HoldingItem:
        "Get a household item by id # Get a household item by id"
        request_path = "/api/v1/holdings/items/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=HoldingItem,
        )

    async def get_insurance_snapshot_endpoint(self, id: str) -> InsuranceSnapshot:
        "Get an insurance snapshot # Get an insurance snapshot with its frozen contents  Every value in the response was materialized at capture. Nothing here is looked up from today's data, so a snapshot reads the same however much the household has changed since."
        request_path = "/api/v1/holdings/insurance-snapshots/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=InsuranceSnapshot,
        )

    async def get_valuation_record_endpoint(self, id: str) -> ValuationRecord:
        "Get a valuation record by id # Get a valuation record by id"
        request_path = "/api/v1/holdings/valuations/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ValuationRecord,
        )

    async def list_holding_items_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None, property_id: str | None = None, room_id: str | None = None, unplaced: bool | None = None, item_kind: str | None = None, category: str | None = None, search: str | None = None, min_value_ore: int | None = None, max_value_ore: int | None = None, include_maintenance: bool | None = None, maintenance: str | None = None, gap: str | None = None, include_document_summary: bool | None = None, include_document_categories: bool | None = None, include_quality: bool | None = None) -> HoldingItemPaginateResponse:
        "List household items # List the items the account can read  Without property_id the result spans every space the caller can read. A property the caller is not a member of is rejected with 403 rather than returned as an empty page.  include_document_summary composes per-item document counts from the file service. It is opt-in because it costs a cross-service call. A null documentSummary means it was not requested or the file service could not be reached, and must not be rendered as \"no documents\"; a summary whose counts are zero is the answer that means that.  include_quality adds the data-quality flags, and implies the document summary and its category breakdown. A null quality follows the same rule: it means \"not evaluated\", never \"nothing missing\"."
        request_path = "/api/v1/holdings/items"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "property_id", property_id, "")
        _add_query(request_query, "room_id", room_id, "")
        _add_query(request_query, "unplaced", unplaced, "")
        _add_query(request_query, "item_kind", item_kind, "")
        _add_query(request_query, "category", category, "")
        _add_query(request_query, "search", search, "")
        _add_query(request_query, "min_value_ore", min_value_ore, "")
        _add_query(request_query, "max_value_ore", max_value_ore, "")
        _add_query(request_query, "include_maintenance", include_maintenance, "")
        _add_query(request_query, "maintenance", maintenance, "")
        _add_query(request_query, "gap", gap, "")
        _add_query(request_query, "include_document_summary", include_document_summary, "")
        _add_query(request_query, "include_document_categories", include_document_categories, "")
        _add_query(request_query, "include_quality", include_quality, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=HoldingItemPaginateResponse,
        )

    async def list_insurance_exports_endpoint(self, id: str) -> InsuranceExportListResponse:
        "List exports of a snapshot # List the reports taken of one snapshot  An audit trail of who exported a household's contents and when. The reports themselves are regenerated on demand rather than stored."
        request_path = "/api/v1/holdings/insurance-snapshots/{id}/exports"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=InsuranceExportListResponse,
        )

    async def list_insurance_snapshots_endpoint(self, space_id: str, *, property_id: str | None = None) -> InsuranceSnapshotListResponse:
        "List insurance snapshots # List the insurance snapshots of a space or one property  Newest first. Frozen contents are not included: they are large and belong to the detail view, and a list is for choosing which snapshot to open."
        request_path = "/api/v1/holdings/insurance-snapshots"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "property_id", property_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=InsuranceSnapshotListResponse,
        )

    async def list_valuation_records_endpoint(self, subject_type: str, subject_id: str, *, valuation_type: str | None = None, as_of_before: str | None = None) -> ValuationRecordListResponse:
        "List the valuation history of one subject # List the valuation history of one subject  subject_type and subject_id are both required: a history is always about one property or one item. Records are returned newest first by asOf, which is when the figure was true rather than when it was entered."
        request_path = "/api/v1/holdings/valuations"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "subject_type", subject_type, "")
        _add_query(request_query, "subject_id", subject_id, "")
        _add_query(request_query, "valuation_type", valuation_type, "")
        _add_query(request_query, "as_of_before", as_of_before, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ValuationRecordListResponse,
        )

    async def move_holding_item_endpoint(self, id: str, *, body: MoveHoldingItemRequest | None = None) -> HoldingItem:
        "Move a household item # Move a household item to another property and/or room  Authorizes against both the source and the target property. Pass a null roomId to leave the item unplaced in the target property."
        request_path = "/api/v1/holdings/items/{id}/move"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=HoldingItem,
        )

    async def update_holding_item_endpoint(self, id: str, *, body: PatchHoldingItemRequest | None = None) -> HoldingItem:
        "Update a household item by id # Update a household item by id  Only the fields in the patch body can be changed. spaceId, propertyId and roomId are not writable; moving an item is a separate operation."
        request_path = "/api/v1/holdings/items/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=HoldingItem,
        )


class ImageApi:
    "Image endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_image_endpoint(self, *, body: CreateImageRequest | None = None, file: FileValue | None = None, source: str | None = None, provider: str | None = None, alt_text: str | None = None, url: str | None = None, meta: str | None = None, public: bool | None = None) -> ImageModel:
        "Create a new image # Create a new image"
        request_path = "/api/v1/attachments/images"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        if file is not None:
            request_files["file"] = file
        if source is not None:
            request_form["Source"] = source
        if provider is not None:
            request_form["Provider"] = provider
        if alt_text is not None:
            request_form["AltText"] = alt_text
        if url is not None:
            request_form["URL"] = url
        if meta is not None:
            request_form["Meta"] = meta
        if public is not None:
            request_form["Public"] = public
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=ImageModel,
        )

    async def delete_image_endpoint(self, id: str) -> None:
        "Delete a image by id # Delete a image by id"
        request_path = "/api/v1/attachments/images/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_image_endpoint(self, id: str) -> ImageModel:
        "Get a image by id # Get a image by id"
        request_path = "/api/v1/attachments/images/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ImageModel,
        )

    async def get_images_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> ImagePaginateResponse:
        "Get all images # Get all images"
        request_path = "/api/v1/attachments/images"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ImagePaginateResponse,
        )

    async def update_image_endpoint(self, id: str, *, body: ImageModel | None = None) -> ImageModel:
        "Update a image by id # Update a image by id"
        request_path = "/api/v1/attachments/images/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ImageModel,
        )


class ImportsApi:
    "Imports endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def cancel_import_draft_endpoint(self, id: str) -> KobleImportJob:
        "Abandon a review draft and remove the object it created. Idempotent: a second cancel of the same draft succeeds."
        request_path = "/api/v1/imports/{id}/cancel"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleImportJob,
        )

    async def confirm_import_endpoint(self, id: str) -> KobleImportJob:
        "Activate a reviewed draft. Field corrections use the regular PATCH endpoint before confirmation and are retained as user-override evidence."
        request_path = "/api/v1/imports/{id}/confirm"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleImportJob,
        )

    async def get_import_endpoint(self, id: str) -> KobleImportJob:
        "Get import processing and review status."
        request_path = "/api/v1/imports/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleImportJob,
        )

    async def registry_journey_endpoint(self, body: KobleRegistryLookupRequest) -> KobleImportJob:
        "Look up a registration number or VIN and work out for itself whether it is a car, caravan or supported trailer. Returns a review draft with entityType and entityId. Send idempotencyKey so a retry returns the same draft rather than registering the object twice. When the registry does not describe the object clearly enough, responds 400 and the caller should use the typed lookup."
        request_path = "/api/v1/registry/lookup"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleImportJob,
        )

    async def rerun_import_endpoint(self, id: str) -> KobleImportJob:
        "Re-process a failed import with the current parser chain — URL imports fetch again, uploaded sources re-parse the retained original."
        request_path = "/api/v1/imports/{id}/rerun"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleImportJob,
        )


class InvitationApi:
    "Invitation endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def accept_invitation_endpoint(self, *, body: AcceptInvitationRequest | None = None) -> Invitation:
        "Accept invitation # Accept invitation"
        request_path = "/api/v1/invitations/accept"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Invitation,
        )

    async def get_invitations_endpoint(self) -> list[Invitation]:
        "Get all invitations # Get all invitations"
        request_path = "/api/v1/invitations/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Invitation],
        )


class ListApi:
    "List endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_list_endpoint(self, *, body: CreateListRequest | None = None) -> ListModel:
        "Create a new list # Create a new list"
        request_path = "/api/v1/lists"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ListModel,
        )

    async def delete_list_endpoint(self, id: str) -> None:
        "Delete a list by id # Delete a list by id"
        request_path = "/api/v1/lists/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_list_endpoint(self, id: str, *, include_items: bool | None = None) -> ListModel:
        "Get a list by id # Get a list by id"
        request_path = "/api/v1/lists/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "include_items", include_items, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ListModel,
        )

    async def get_list_members_endpoint(self, id: str) -> list[ListUserLink]:
        "Get all list members # Get all list members"
        request_path = "/api/v1/lists/{id}/members"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[ListUserLink],
        )

    async def get_lists_endpoint(self, *, space_id: str | None = None, list_type: list[str] | None = None) -> list[ListModel]:
        "Get all lists # Get all lists"
        request_path = "/api/v1/lists"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "list_type", list_type, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[ListModel],
        )

    async def get_lists_endpoint_v2(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None, list_type: list[str] | None = None) -> ListPaginateResponse:
        "Get all lists # Get all lists"
        request_path = "/api/v2/lists"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "list_type", list_type, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ListPaginateResponse,
        )

    async def mute_list_endpoint(self, id: str, *, mute_until: str | None = None) -> None:
        "Mute list notifications # Mute list notifications"
        request_path = "/api/v1/lists/{id}/mute"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "mute_until", mute_until, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def set_should_notify_list_endpoint(self, id: str, should_notify: bool) -> None:
        "Set should notify setting for list notifications # Set should notify setting for list notifications"
        request_path = "/api/v1/lists/{id}/set-should-notify"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "should_notify", should_notify, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def un_mute_list_endpoint(self, id: str) -> None:
        "Un mute list notifications # Un mute list notifications"
        request_path = "/api/v1/lists/{id}/un-mute"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def update_list_endpoint(self, id: str, *, body: ListModel | None = None) -> ListModel:
        "Update a list by id # Update a list by id"
        request_path = "/api/v1/lists/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ListModel,
        )

    async def update_list_members_endpoint(self, id: str, *, body: list[ListUserLink] | None = None) -> list[ListUserLink]:
        "Update list members # Update list members"
        request_path = "/api/v1/lists/{id}/members"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[ListUserLink],
        )


class ListItemApi:
    "ListItem endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def autocomplete_list_item_endpoint(self, list_id: str, *, filter: str | None = None, query: str | None = None) -> ProductRecommendations:
        "Autocomplete # Get list item autocomplete items Deprecated."
        request_path = "/api/v1/lists/{list_id}/autocomplete"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "query", query, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ProductRecommendations,
        )

    async def batch_storage_list_suggestion_endpoint(self, space_id: str, *, body: StorageListSuggestionBatchRequest | None = None) -> list[StorageListSuggestion]:
        "Get storage list suggestions # Get storage list suggestions for products"
        request_path = "/api/v1/lists/storage-suggestion"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[StorageListSuggestion],
        )

    async def create_list_item_endpoint(self, list_id: str, *, body: ListItem | None = None, combine_same_items: bool | None = None) -> ListItem:
        "Create a new list item # Create a new list item"
        request_path = "/api/v1/lists/{list_id}/items"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "combine_same_items", combine_same_items, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ListItem,
        )

    async def delete_list_item_endpoint(self, list_id: str, item_id: str) -> None:
        "Deletes a list item by id # Deletes a list item by id"
        request_path = "/api/v1/lists/{list_id}/items/{item_id}"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_path = request_path.replace("{item_id}", quote(_query_value(item_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_list_history_endpoint(self, list_id: str, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None) -> ListItemHistoryPaginateResponse:
        "Get list item history # Get list history for all list items"
        request_path = "/api/v1/lists/{list_id}/history"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ListItemHistoryPaginateResponse,
        )

    async def get_list_item_endpoint(self, list_id: str, item_id: str) -> ListItem:
        "Get a list item by id # Get a list item by id"
        request_path = "/api/v1/lists/{list_id}/items/{item_id}"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_path = request_path.replace("{item_id}", quote(_query_value(item_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ListItem,
        )

    async def get_list_items_by_groups_endpoint(self, list_id: str, *, sort_type: str | None = None, session_id: str | None = None) -> list[GroupedListItemResult]:
        "Get list items by groups # Get list items by groups"
        request_path = "/api/v1/lists/{list_id}/items-by-groups"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "sort_type", sort_type, "")
        _add_query(request_query, "session_id", session_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[GroupedListItemResult],
        )

    async def get_list_items_endpoint(self, list_id: str, *, include_done: bool | None = None) -> list[ListItem]:
        "Get list items # Get list items"
        request_path = "/api/v1/lists/{list_id}/items"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "include_done", include_done, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[ListItem],
        )

    async def get_storage_list_suggestion_endpoint(self, space_id: str, *, product_ref: str | None = None, product_category_ref: str | None = None) -> StorageListSuggestion:
        "Get storage list suggestion # Get storage list suggestion for a product"
        request_path = "/api/v1/lists/storage-suggestion"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "product_ref", product_ref, "")
        _add_query(request_query, "product_category_ref", product_category_ref, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StorageListSuggestion,
        )

    async def recommend_list_item_endpoint(self, list_id: str) -> ProductRecommendations:
        "Recommend # Get recommended list items"
        request_path = "/api/v1/lists/{list_id}/recommend"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ProductRecommendations,
        )

    async def set_list_item_done_endpoint(self, list_id: str, item_id: str, *, session_id: str | None = None) -> None:
        "Set list item done # Update a list item by id set it done"
        request_path = "/api/v1/lists/{list_id}/items/{item_id}/done"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_path = request_path.replace("{item_id}", quote(_query_value(item_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "session_id", session_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def set_list_item_quantity_endpoint(self, list_id: str, item_id: str, quantity: float) -> None:
        "Set list item quantity # Update a list item by id set quantity"
        request_path = "/api/v1/lists/{list_id}/items/{item_id}/set-quantity"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_path = request_path.replace("{item_id}", quote(_query_value(item_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "quantity", quantity, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def sort_list_item_endpoint(self, list_id: str, *, body: list[SortOrderRequest] | None = None) -> list[ListItem]:
        "Sort # Sorts list items"
        request_path = "/api/v1/lists/{list_id}/sort"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[ListItem],
        )

    async def update_list_item_endpoint(self, list_id: str, item_id: str, *, body: ListItem | None = None) -> ListItem:
        "Update a list item by id # Update a list item by id"
        request_path = "/api/v1/lists/{list_id}/items/{item_id}"
        request_path = request_path.replace("{list_id}", quote(_query_value(list_id), safe=""))
        request_path = request_path.replace("{item_id}", quote(_query_value(item_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ListItem,
        )


class LocalesApi:
    "Locales endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def get_locales_endpoint(self) -> None:
        "Get locales # Get locales"
        request_path = "/api/v1/supporting/localize/locales/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=None,
        )

    async def get_localize_endpoint(self, domain: str, key: str, *, lang: str | None = None, placeholders: str | None = None) -> None:
        "Get localize key # Get localize key"
        request_path = "/api/v1/supporting/localize/localize/{domain}/{key}"
        request_path = request_path.replace("{domain}", quote(_query_value(domain), safe=""))
        request_path = request_path.replace("{key}", quote(_query_value(key), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "lang", lang, "")
        _add_query(request_query, "placeholders", placeholders, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=None,
        )


class MealApi:
    "Meal endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_meal_endpoint(self, *, body: Meal | None = None) -> Meal:
        "Create a new meal # Create a new meal Deprecated."
        request_path = "/api/v1/meal-planner/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Meal,
        )

    async def delete_meal_endpoint(self, meal_id: str) -> None:
        "Deletes a meal by id # Deletes a meal by id Deprecated."
        request_path = "/api/v1/meal-planner/{meal_id}"
        request_path = request_path.replace("{meal_id}", quote(_query_value(meal_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_meal_endpoint(self, meal_id: str) -> Meal:
        "Get a meal by id # Get a meal by id Deprecated."
        request_path = "/api/v1/meal-planner/{meal_id}"
        request_path = request_path.replace("{meal_id}", quote(_query_value(meal_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Meal,
        )

    async def get_meals_endpoint(self, *, space_id: str | None = None, from_date: str | None = None, to_date: str | None = None, meal_type: str | None = None) -> list[Meal]:
        "Get all meals # Get all meals Deprecated."
        request_path = "/api/v1/meal-planner/"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "from_date", from_date, "")
        _add_query(request_query, "to_date", to_date, "")
        _add_query(request_query, "meal_type", meal_type, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Meal],
        )

    async def update_meal_endpoint(self, meal_id: str, *, body: Meal | None = None) -> Meal:
        "Update a meal by id # Update a meal by id Deprecated."
        request_path = "/api/v1/meal-planner/{meal_id}"
        request_path = request_path.replace("{meal_id}", quote(_query_value(meal_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Meal,
        )


class MealPlannerApi:
    "MealPlanner endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_meal_slot_endpoint(self, *, body: CreateMealSlotRequest | None = None) -> MealSlot:
        "Create a new meal slot # Create a new meal slot"
        request_path = "/api/v1/meal-planner/meal-slots"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=MealSlot,
        )

    async def delete_meal_slot_endpoint(self, id: str) -> None:
        "Delete a meal slot by id # Delete a meal slot by id"
        request_path = "/api/v1/meal-planner/meal-slots/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_meal_slot_endpoint(self, id: str) -> MealSlot:
        "Get a meal slot by id # Get a meal slot by id"
        request_path = "/api/v1/meal-planner/meal-slots/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=MealSlot,
        )

    async def get_meal_slots_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None, from_date: str | None = None, to_date: str | None = None, meal_type: str | None = None) -> MealSlotPaginateResponse:
        "Get all meal slots # Get all meal slots"
        request_path = "/api/v1/meal-planner/meal-slots"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "from_date", from_date, "")
        _add_query(request_query, "to_date", to_date, "")
        _add_query(request_query, "meal_type", meal_type, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=MealSlotPaginateResponse,
        )

    async def get_meals_calendar_endpoint(self) -> None:
        "Get all meals in iCal format # Get all meals in iCal format"
        request_path = "/api/v1/meal-planner/calendar.ics"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_most_used_meals_endpoint(self, *, space_id: str | None = None, limit: int | None = None) -> list[Recipe]:
        "Get the most used meals in a space # Get the most used meals in a space"
        request_path = "/api/v1/meal-planner/most-used"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "limit", limit, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Recipe],
        )

    async def plan_week_endpoint(self, *, body: WeekPlanOptions | None = None) -> list[PlannedSlot]:
        "Get the meal plan for the week # Get the meal plan for the week"
        request_path = "/api/v1/meal-planner/plan"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[PlannedSlot],
        )

    async def update_meal_slot_endpoint(self, id: str, *, body: MealSlot | None = None) -> MealSlot:
        "Update a meal slot by id # Update a meal slot by id"
        request_path = "/api/v1/meal-planner/meal-slots/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=MealSlot,
        )


class MetadataApi:
    "Metadata endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def get_metadata_endpoint(self, key: str) -> Metadata:
        "Get metadata # Get account metadata by key"
        request_path = "/api/v1/access/metadata/{key}"
        request_path = request_path.replace("{key}", quote(_query_value(key), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Metadata,
        )

    async def update_metadata_endpoint(self, key: str, *, body: str | None = None) -> Metadata:
        "Create or update # Creates or updates account metadata"
        request_path = "/api/v1/access/metadata/{key}"
        request_path = request_path.replace("{key}", quote(_query_value(key), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Metadata,
        )


class NewsletterApi:
    "Newsletter endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_newsletter_endpoint(self, *, body: CreateNewsletterRequest | None = None) -> Newsletter:
        "Create a new newsletter # Create a new newsletter"
        request_path = "/api/v1/supporting/newsletters"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Newsletter,
        )

    async def delete_newsletter_endpoint(self, id: str) -> None:
        "Delete a newsletter by id # Delete a newsletter by id"
        request_path = "/api/v1/supporting/newsletters/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_newsletter_endpoint(self, id: str) -> Newsletter:
        "Get a newsletter by id # Get a newsletter by id"
        request_path = "/api/v1/supporting/newsletters/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Newsletter,
        )

    async def get_newsletters_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> NewsletterPaginateResponse:
        "Get all newsletters # Get all newsletters"
        request_path = "/api/v1/supporting/newsletters"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=NewsletterPaginateResponse,
        )

    async def update_newsletter_endpoint(self, id: str, *, body: CreateNewsletterRequest | None = None) -> Newsletter:
        "Update a newsletter by id # Update a newsletter by id"
        request_path = "/api/v1/supporting/newsletters/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Newsletter,
        )


class NotificationApi:
    "Notification endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_notification_endpoint(self, *, body: Notification | None = None) -> Notification:
        "Create a new notification # Create a new notification"
        request_path = "/api/v1/supporting/notifications/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Notification,
        )

    async def delete_notification_endpoint(self, notification_id: str) -> None:
        "Deletes a notification by id # Deletes a notification by id"
        request_path = "/api/v1/supporting/notifications/{notification_id}"
        request_path = request_path.replace("{notification_id}", quote(_query_value(notification_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_notification_endpoint(self, notification_id: str) -> Notification:
        "Get a notification by id # Get a notification by id"
        request_path = "/api/v1/supporting/notifications/{notification_id}"
        request_path = request_path.replace("{notification_id}", quote(_query_value(notification_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Notification,
        )

    async def get_notification_setting_endpoint(self) -> NotificationSetting:
        "Get a notification setting # Get a notification setting"
        request_path = "/api/v1/supporting/notifications/settings"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=NotificationSetting,
        )

    async def get_notifications_endpoint(self) -> list[Notification]:
        "Get all notifications # Get all notifications"
        request_path = "/api/v1/supporting/notifications/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Notification],
        )

    async def get_unsubscribe_newsletter_endpoint(self) -> None:
        "Unsubscribe from newsletter # Unsubscribe from newsletter"
        request_path = "/api/v1/unsubscribe"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=None,
        )

    async def update_notification_endpoint(self, notification_id: str, *, body: Notification | None = None) -> Notification:
        "Update a notification by id # Update a notification by id"
        request_path = "/api/v1/supporting/notifications/{notification_id}"
        request_path = request_path.replace("{notification_id}", quote(_query_value(notification_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Notification,
        )

    async def update_notification_setting_endpoint(self, *, body: NotificationSetting | None = None) -> NotificationSetting:
        "Update a notification setting # Update a notification setting"
        request_path = "/api/v1/supporting/notifications/settings"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=NotificationSetting,
        )


class PlacementsApi:
    "Placements endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_placement_endpoint(self, body: CreatePlacementRequest) -> ExternalHoldingPlacement:
        "Record that an external object stands at a property. Requires write access to the property and read access to the referenced object. The object itself is not copied — only a reference to it is stored."
        request_path = "/api/v1/holdings/placements"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ExternalHoldingPlacement,
        )

    async def delete_placement_endpoint(self, id: str) -> None:
        "Forget where an external object stood. The object itself is untouched."
        request_path = "/api/v1/holdings/placements/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_placement_endpoint(self, id: str) -> ExternalHoldingPlacement:
        "Get one placement."
        request_path = "/api/v1/holdings/placements/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ExternalHoldingPlacement,
        )

    async def list_property_placements_endpoint(self, id: str) -> list[ExternalHoldingPlacement]:
        "List the external objects standing at one property. Only the objects the caller can still read are returned; a reference whose object has been unshared or deleted is omitted rather than shown as a bare id."
        request_path = "/api/v1/holdings/properties/{id}/placements"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[ExternalHoldingPlacement],
        )

    async def patch_placement_endpoint(self, id: str, body: PatchPlacementRequest) -> ExternalHoldingPlacement:
        "Move a placement to another property or room, or edit its note. The external reference cannot be changed; place a different object instead."
        request_path = "/api/v1/holdings/placements/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ExternalHoldingPlacement,
        )


class ProductApi:
    "Product endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def autocomplete_product_endpoint(self, *, filter: str | None = None, query: str | None = None, list_id: str | None = None) -> ProductRecommendations:
        "Autocomplete products # Get product autocomplete items"
        request_path = "/api/v1/shopping/products/autocomplete"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "query", query, "")
        _add_query(request_query, "list_id", list_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ProductRecommendations,
        )

    async def create_product_endpoint(self, *, body: Product | None = None) -> Product:
        "Create a new product # Create a new product"
        request_path = "/api/v1/shopping/products"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Product,
        )

    async def delete_product_endpoint(self, id: str) -> None:
        "Deletes a product by id # Deletes a product by id"
        request_path = "/api/v1/shopping/products/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_product_ean_endpoint(self, gtin: str) -> Product:
        "Get a product by GTIN # Get a product by GTIN"
        request_path = "/api/v1/shopping/products/ean/{GTIN}"
        request_path = request_path.replace("{GTIN}", quote(_query_value(gtin), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Product,
        )

    async def get_product_endpoint(self, id: str, *, detailed: bool | None = None) -> Product:
        "Get a product by id # Get a product by id"
        request_path = "/api/v1/shopping/products/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "detailed", detailed, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Product,
        )

    async def get_products_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> ProductPaginateResponse:
        "Get all products # Get all products"
        request_path = "/api/v1/shopping/products"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ProductPaginateResponse,
        )

    async def get_type_ahead_brands_endpoint(self, *, query: str | None = None) -> list[str]:
        "Autocomplete Brands # Get list of brands for autocomplete"
        request_path = "/api/v1/shopping/brands/type-ahead"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "query", query, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[str],
        )

    async def get_vendor_gtin_prefix_endpoint(self) -> None:
        "Get a vendor by GTIN Prefix # Get a vendor by GTIN Prefix"
        request_path = "/api/v1/shopping/products/ean/lookup-prefix/{GTINPrefix}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def insight_product_prices_endpoint(self, id: str) -> ProductPriceInsights:
        "Insight product prices # Insight product prices"
        request_path = "/api/v1/shopping/products/{id}/insight/price"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ProductPriceInsights,
        )

    async def insight_product_reorder_cadence_endpoint(self, *, space_id: str | None = None, list_id: str | None = None, limit: int | None = None) -> list[ProductReorderCadence]:
        "Insight product reorder cadence # Insight product reorder cadence"
        request_path = "/api/v1/shopping/products/insight/reorder-cadence"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "list_id", list_id, "")
        _add_query(request_query, "limit", limit, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[ProductReorderCadence],
        )

    async def log_searchkey_endpoint(self, *, body: ProductSearchKey | None = None) -> None:
        "Log search key # Log search key for analytics purposes"
        request_path = "/api/v1/shopping/products/log-searchkey"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def lookup_product_ean_endpoint(self, gtin: str) -> ProductGTINLookupResponse:
        "Look up a product by GTIN # Look up a product by GTIN"
        request_path = "/api/v1/shopping/products/ean/lookup/{GTIN}"
        request_path = request_path.replace("{GTIN}", quote(_query_value(gtin), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ProductGTINLookupResponse,
        )

    async def post_scan_product_endpoint(self, *, body: NewProductScanRequestModel | None = None) -> NewProductScanRequestModel:
        "Scan after product # Scan after product"
        request_path = "/api/v1/shopping/products/scanner/start"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=NewProductScanRequestModel,
        )

    async def search_products_endpoint(self, query: str, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None) -> ProductPaginateResponse:
        "Search products # Search products"
        request_path = "/api/v1/shopping/products/search/{query}"
        request_path = request_path.replace("{query}", quote(_query_value(query), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ProductPaginateResponse,
        )

    async def update_product_endpoint(self, id: str, *, body: Product | None = None) -> Product:
        "Update a product by id # Update a product by id"
        request_path = "/api/v1/shopping/products/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Product,
        )

    async def upload_scan_product_image_endpoint(self, *, file: FileValue | None = None, gtin: str | None = None, image_side: str | None = None) -> ProductImageScanRequest:
        "Uploads a product image # Uploads a product image"
        request_path = "/api/v1/shopping/products/scanner/upload"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        if file is not None:
            request_files["file"] = file
        if gtin is not None:
            request_form["gtin"] = gtin
        if image_side is not None:
            request_form["image_side"] = image_side
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=ProductImageScanRequest,
        )


class ProductCategoryApi:
    "ProductCategory endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_product_category_endpoint(self, *, body: ProductCategory | None = None) -> ProductCategory:
        "Create a new product category # Create a new product category"
        request_path = "/api/v1/shopping/categories"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ProductCategory,
        )

    async def delete_product_category_endpoint(self, id: str) -> None:
        "Deletes a product category by id # Deletes a product category by id"
        request_path = "/api/v1/shopping/categories/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_product_categories_endpoint(self, *, parent_id: str | None = None) -> list[ProductCategoryResult]:
        "Get all product categories # Get all product categories"
        request_path = "/api/v1/shopping/categories"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "parent_id", parent_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=list[ProductCategoryResult],
        )

    async def get_product_category_endpoint(self, id: str) -> ProductCategory:
        "Get a product category by id # Get a product category by id"
        request_path = "/api/v1/shopping/categories/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=ProductCategory,
        )

    async def get_product_category_tree_endpoint(self, id: str) -> list[ProductCategory]:
        "Get a product category tree by id Get a product category tree by id"
        request_path = "/api/v1/shopping/categories/{id}/tree"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=list[ProductCategory],
        )

    async def update_product_category_endpoint(self, id: str, *, body: ProductCategory | None = None) -> ProductCategory:
        "Update a product category by id # Update a product category by id"
        request_path = "/api/v1/shopping/categories/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ProductCategory,
        )


class PropertyApi:
    "Property endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_property_endpoint(self, *, body: CreatePropertyRequest | None = None) -> Property:
        "Create a new property # Create a new property"
        request_path = "/api/v1/holdings/properties"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Property,
        )

    async def create_property_room_endpoint(self, property_id: str, *, body: CreatePropertyRoomRequest | None = None) -> PropertyRoom:
        "Create a new property room # Create a new property room"
        request_path = "/api/v1/holdings/properties/{property_id}/rooms"
        request_path = request_path.replace("{property_id}", quote(_query_value(property_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=PropertyRoom,
        )

    async def delete_property_endpoint(self, id: str) -> None:
        "Delete a property by id # Delete a property by id"
        request_path = "/api/v1/holdings/properties/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_property_room_endpoint(self, id: str, property_id: str) -> None:
        "Delete a property room by id # Delete a property room by id"
        request_path = "/api/v1/holdings/properties/{property_id}/rooms/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{property_id}", quote(_query_value(property_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_properties_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None) -> PropertyPaginateResponse:
        "Get all properties # Get all properties in a space the account is a member of"
        request_path = "/api/v1/holdings/properties"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=PropertyPaginateResponse,
        )

    async def get_property_endpoint(self, id: str) -> Property:
        "Get a property by id # Get a property by id"
        request_path = "/api/v1/holdings/properties/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Property,
        )

    async def get_property_room_endpoint(self, id: str, property_id: str) -> PropertyRoom:
        "Get a property room by id # Get a property room by id"
        request_path = "/api/v1/holdings/properties/{property_id}/rooms/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{property_id}", quote(_query_value(property_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=PropertyRoom,
        )

    async def get_property_rooms_endpoint(self, property_id: str, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> PropertyRoomPaginateResponse:
        "Get all property rooms # Get all rooms of a property the account can read"
        request_path = "/api/v1/holdings/properties/{property_id}/rooms"
        request_path = request_path.replace("{property_id}", quote(_query_value(property_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=PropertyRoomPaginateResponse,
        )

    async def update_property_endpoint(self, id: str, *, body: PatchPropertyRequest | None = None) -> Property:
        "Update a property by id # Update a property by id  Only the fields in the patch body can be changed. spaceId, rooms, owners and the audit fields are not writable; moving a property between spaces is a separate, explicit operation."
        request_path = "/api/v1/holdings/properties/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Property,
        )

    async def update_property_room_endpoint(self, id: str, property_id: str, *, body: PatchPropertyRoomRequest | None = None) -> PropertyRoom:
        "Update a property room by id # Update a property room by id  Only the fields in the patch body can be changed. propertyId and the audit fields are not writable; moving a room to another property is a separate, explicit operation."
        request_path = "/api/v1/holdings/properties/{property_id}/rooms/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{property_id}", quote(_query_value(property_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=PropertyRoom,
        )


class ReferralApi:
    "Referral endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_referral_endpoint(self, *, body: CreateReferralRequest | None = None) -> Referral:
        "Create a new referral # Create a new referral"
        request_path = "/api/v1/supporting/referrals"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Referral,
        )

    async def delete_referral_endpoint(self, id: str) -> None:
        "Delete a referral by id # Delete a referral by id"
        request_path = "/api/v1/supporting/referrals/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_app_invite_referral_endpoint(self) -> AppInviteReferralResponse:
        "Get or create app invite referral for current user # Get or create app invite referral for current user"
        request_path = "/api/v1/supporting/referrals/app-invite"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=AppInviteReferralResponse,
        )

    async def get_app_invite_reward_status_endpoint(self) -> AppInviteRewardStatusResponse:
        "Get app invite reward status for current user # Get app invite reward status for current user"
        request_path = "/api/v1/supporting/referrals/app-invite/status"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=AppInviteRewardStatusResponse,
        )

    async def get_referral_endpoint(self, code: str) -> Referral:
        "Get a referral by code # Get a referral by code"
        request_path = "/api/v1/supporting/referrals/{code}"
        request_path = request_path.replace("{code}", quote(_query_value(code), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=Referral,
        )

    async def get_referrals_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, include_details: bool | None = None) -> ReferralPaginateResponse:
        "Get all referrals # Get all referrals"
        request_path = "/api/v1/supporting/referrals"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "include_details", include_details, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ReferralPaginateResponse,
        )

    async def redeem_app_invite_referral_endpoint(self, *, body: RegisterAppInviteReferralRequest | None = None) -> RegisterAppInviteReferralResponse:
        "Register app invite referral signup for current user # Register app invite referral signup for current user"
        request_path = "/api/v1/supporting/referrals/app-invite/redeem"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=RegisterAppInviteReferralResponse,
        )

    async def update_referral_endpoint(self, id: str, *, body: Referral | None = None) -> Referral:
        "Update a referral by id # Update a referral by id"
        request_path = "/api/v1/supporting/referrals/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Referral,
        )


class SenderApi:
    "Sender endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def email_postmark_callback_endpoint(self) -> None:
        "Callback for postmark app webhook # Callback for postmark app webhook"
        request_path = "/api/v1/sender/email/postmark/callback/{action}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=None,
        )

    async def open_message_endpoint(self, id: str) -> None:
        "Callback for opened message # Callback for opened message"
        request_path = "/api/v1/sender/messages/opened/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def preview_email_endpoint(self) -> None:
        "Preview a email # Preview a email"
        request_path = "/api/v1/sender/email/{id}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def send_test_notification_endpoint(self, *, body: SendFCMEvent | None = None) -> None:
        "Send test push notification # Send test push notification"
        request_path = "/api/v1/sender/fcm/send-test-notification"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )


class SessionApi:
    "Session endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_session_endpoint(self, *, body: ShoppingSession | None = None) -> ShoppingSession:
        "Create a new session # Create a new session"
        request_path = "/api/v1/shopping/sessions/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ShoppingSession,
        )

    async def delete_session_endpoint(self, session_id: str) -> None:
        "Deletes a session by id # Deletes a session by id"
        request_path = "/api/v1/shopping/sessions/{session_id}"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def end_session_endpoint(self, session_id: str) -> ShoppingSession:
        "End session # End session"
        request_path = "/api/v1/shopping/sessions/{session_id}/end"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ShoppingSession,
        )

    async def get_session_endpoint(self, session_id: str, *, space_id: str | None = None) -> ShoppingSession:
        "Get a session by id # Get a session by id"
        request_path = "/api/v1/shopping/sessions/{session_id}"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ShoppingSession,
        )

    async def get_session_insight_category_breakdown_endpoint(self, *, space_id: str | None = None, list_id: str | None = None) -> list[SessionInsightCategoryBreakdown]:
        "Get session insight category breakdown # Get session insight category breakdown"
        request_path = "/api/v1/shopping/sessions/insight/category-breakdown"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "list_id", list_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SessionInsightCategoryBreakdown],
        )

    async def get_session_insight_dow_endpoint(self, space_id: str) -> list[SessionInsight]:
        "Get sessions by day of week # Get sessions by day of week"
        request_path = "/api/v1/shopping/sessions/insight/dow"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SessionInsight],
        )

    async def get_session_insight_summary_endpoint(self, *, space_id: str | None = None, list_id: str | None = None, top_store_limit: int | None = None) -> SessionInsightSummary:
        "Get session insight summary # Get session insight summary"
        request_path = "/api/v1/shopping/sessions/insight/summary"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "list_id", list_id, "")
        _add_query(request_query, "top_store_limit", top_store_limit, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SessionInsightSummary,
        )

    async def get_session_insight_time_series_endpoint(self, *, space_id: str | None = None, list_id: str | None = None, granularity: str | None = None, start_at: str | None = None, end_at: str | None = None) -> list[SessionInsightTimeSeriesPoint]:
        "Get session insight time series # Get session insight time series"
        request_path = "/api/v1/shopping/sessions/insight/time-series"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "list_id", list_id, "")
        _add_query(request_query, "granularity", granularity, "")
        _add_query(request_query, "start_at", start_at, "")
        _add_query(request_query, "end_at", end_at, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SessionInsightTimeSeriesPoint],
        )

    async def get_session_insight_top_products_endpoint(self, space_id: str) -> list[Product]:
        "Get top product from sessions # Get top product from sessions"
        request_path = "/api/v1/shopping/sessions/insight/top-products"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Product],
        )

    async def get_session_insight_top_stores_endpoint(self, *, space_id: str | None = None, list_id: str | None = None, limit: int | None = None) -> list[SessionStoreInsight]:
        "Get session insight top stores # Get session insight top stores"
        request_path = "/api/v1/shopping/sessions/insight/top-stores"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "list_id", list_id, "")
        _add_query(request_query, "limit", limit, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SessionStoreInsight],
        )

    async def get_session_insight_user_contributions_endpoint(self, *, space_id: str | None = None, list_id: str | None = None) -> list[SessionUserContribution]:
        "Get session insight user contributions # Get session insight user contributions"
        request_path = "/api/v1/shopping/sessions/insight/user-contributions"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "list_id", list_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SessionUserContribution],
        )

    async def get_session_list_dow_endpoint(self) -> list[SessionDoW]:
        "Get day of week from sessions by list id # Get day of week from sessions by list id"
        request_path = "/api/v1/shopping/sessions/list/day-of-week"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SessionDoW],
        )

    async def get_session_list_pick_occurrences_endpoint(self, list_id: str) -> ListItemInsightRecommendations:
        "Get recommended products by pick occurrences and list id # Get recommended products by pick occurrences and list id"
        request_path = "/api/v1/shopping/sessions/list/pick-occurrences"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "list_id", list_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ListItemInsightRecommendations,
        )

    async def get_session_receipt_lines_endpoint(self, session_id: str) -> list[ShoppingSessionReceiptLine]:
        "Get session receipt lines # Get session receipt lines"
        request_path = "/api/v1/shopping/sessions/{session_id}/receipt/lines"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[ShoppingSessionReceiptLine],
        )

    async def get_sessions_endpoint(self, *, space_id: str | None = None, list_id: str | None = None) -> list[AllShoppingSessionResponse]:
        "Get all sessions # Get all sessions"
        request_path = "/api/v1/shopping/sessions/"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "list_id", list_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[AllShoppingSessionResponse],
        )

    async def match_session_receipt_line_endpoint(self, session_id: str, line_id: str, *, body: MatchShoppingSessionReceiptLineRequest | None = None) -> ShoppingSessionReceiptLine:
        "Match session receipt line to item pick # Match session receipt line to item pick"
        request_path = "/api/v1/shopping/sessions/{session_id}/receipt/lines/{line_id}"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_path = request_path.replace("{line_id}", quote(_query_value(line_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ShoppingSessionReceiptLine,
        )

    async def register_activity_token_endpoint(self, session_id: str, *, body: RegisterActivityTokenRequest | None = None) -> None:
        "Register activity token # Register activity token"
        request_path = "/api/v1/shopping/sessions/{session_id}/register-activity-token"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def session_pick_item_endpoint(self, session_id: str, *, body: PickItemShoppingSessionRequest | None = None) -> ShoppingSessionItemPick:
        "Pick item # Pick item and store it in session"
        request_path = "/api/v1/shopping/sessions/{session_id}/pick"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ShoppingSessionItemPick,
        )

    async def session_price_tag_scan_endpoint(self, session_id: str, *, file: FileValue | None = None) -> None:
        "Receive price tag scan image # Receive price tag scan image"
        request_path = "/api/v1/shopping/sessions/{session_id}/price-tag-scan"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        if file is not None:
            request_files["file"] = file
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def start_session_endpoint(self, *, body: StartShoppingSessionRequest | None = None) -> ShoppingSession:
        "Start a new session # Start a new session"
        request_path = "/api/v1/shopping/sessions/start"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ShoppingSession,
        )

    async def update_session_endpoint(self, session_id: str, *, body: ShoppingSession | None = None) -> ShoppingSession:
        "Update a session by id # Update a session by id"
        request_path = "/api/v1/shopping/sessions/{session_id}"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=ShoppingSession,
        )

    async def upload_session_receipt_endpoint(self, session_id: str, file: FileValue) -> ShoppingSessionReceipt:
        "Deprecated: use attachment service instead Upload receipt image to session # Upload receipt image to session"
        request_path = "/api/v1/shopping/sessions/{session_id}/receipt"
        request_path = request_path.replace("{session_id}", quote(_query_value(session_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_files["file"] = file
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=ShoppingSessionReceipt,
        )


class SpaceApi:
    "Space endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def claim_space_reward_endpoint(self, id: str, reward_id: str, *, body: ClaimRewardRequest | None = None) -> SpaceRewardClaim:
        "Claim reward # Claim a reward for a space member"
        request_path = "/api/v1/spaces/{id}/xp/rewards/{rewardId}/claim"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{rewardId}", quote(_query_value(reward_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceRewardClaim,
        )

    async def connect_space_member_account_endpoint(self, id: str, member_id: str, *, body: ConnectSpaceMemberAccountRequest | None = None) -> SpaceMember:
        "Connect account to space member # Connect an invited account to an existing space member"
        request_path = "/api/v1/spaces/{id}/members/{memberId}/connect-account"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{memberId}", quote(_query_value(member_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceMember,
        )

    async def create_space_endpoint(self, *, body: CreateSpaceRequest | None = None) -> Space:
        "Create a new space # Create a new space"
        request_path = "/api/v1/spaces/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Space,
        )

    async def create_space_member_endpoint(self, id: str, *, body: CreateSpaceMemberRequest | None = None) -> SpaceMember:
        "Create space member # Create a new local member in a space"
        request_path = "/api/v1/spaces/{id}/members"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceMember,
        )

    async def create_space_reward_endpoint(self, id: str, *, body: CreateSpaceRewardRequest | None = None) -> SpaceReward:
        "Create space reward # Create a reward definition in a space"
        request_path = "/api/v1/spaces/{id}/xp/rewards"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceReward,
        )

    async def delete_space_endpoint(self, id: str) -> None:
        "Deletes a space by id # Deletes a space by id"
        request_path = "/api/v1/spaces/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_space_member_endpoint(self, id: str, member_id: str) -> None:
        "Delete space member # Delete a space member"
        request_path = "/api/v1/spaces/{id}/members/{memberId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{memberId}", quote(_query_value(member_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_space_reward_endpoint(self, id: str, reward_id: str) -> None:
        "Delete space reward # Delete a reward definition"
        request_path = "/api/v1/spaces/{id}/xp/rewards/{rewardId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{rewardId}", quote(_query_value(reward_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_default_space_endpoint(self) -> Space:
        "Get user account default space # Get user account default space"
        request_path = "/api/v1/spaces/default"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Space,
        )

    async def get_space_account_score_endpoint(self, id: str, *, from_date: str | None = None, to_date: str | None = None) -> list[SpaceAccountScoreResponse]:
        "Score space # Score space"
        request_path = "/api/v1/spaces/{id}/scores"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "from_date", from_date, "")
        _add_query(request_query, "to_date", to_date, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SpaceAccountScoreResponse],
        )

    async def get_space_endpoint(self, id: str, *, invitation_id: str | None = None) -> Space:
        "Get a space by id # Get a space by id"
        request_path = "/api/v1/spaces/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "invitation_id", invitation_id, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Space,
        )

    async def get_space_member_endpoint(self, id: str, member_id: str) -> SpaceMember:
        "Get space member # Get a space member by id"
        request_path = "/api/v1/spaces/{id}/members/{memberId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{memberId}", quote(_query_value(member_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceMember,
        )

    async def get_space_members_endpoint(self, id: str) -> list[SpaceMember]:
        "Get space members # Get all space members"
        request_path = "/api/v1/spaces/{id}/members"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SpaceMember],
        )

    async def get_space_reward_catalog_endpoint(self, id: str, member_id: str) -> list[RewardCatalogEntry]:
        "Get reward catalog # Get reward claimability for a space member"
        request_path = "/api/v1/spaces/{id}/xp/rewards/catalog/{memberId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{memberId}", quote(_query_value(member_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[RewardCatalogEntry],
        )

    async def get_space_reward_claim_endpoint(self, id: str, claim_id: str) -> SpaceRewardClaim:
        "Get reward claim # Get a reward claim by id"
        request_path = "/api/v1/spaces/{id}/xp/rewards/claims/{claimId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{claimId}", quote(_query_value(claim_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceRewardClaim,
        )

    async def get_space_reward_claims_endpoint(self, id: str, *, member_id: str | None = None, reward_id: str | None = None, status: str | None = None, limit: int | None = None) -> list[SpaceRewardClaim]:
        "Get reward claims # Get reward claims for a space"
        request_path = "/api/v1/spaces/{id}/xp/rewards/claims"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "memberId", member_id, "")
        _add_query(request_query, "rewardId", reward_id, "")
        _add_query(request_query, "status", status, "")
        _add_query(request_query, "limit", limit, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SpaceRewardClaim],
        )

    async def get_space_reward_endpoint(self, id: str, reward_id: str) -> SpaceReward:
        "Get space reward # Get a reward definition by id"
        request_path = "/api/v1/spaces/{id}/xp/rewards/{rewardId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{rewardId}", quote(_query_value(reward_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceReward,
        )

    async def get_space_rewards_endpoint(self, id: str, *, include_inactive: bool | None = None) -> list[SpaceReward]:
        "Get space rewards # Get reward definitions for a space"
        request_path = "/api/v1/spaces/{id}/xp/rewards"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "include_inactive", include_inactive, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SpaceReward],
        )

    async def get_space_score_history_endpoint(self, id: str, *, limit: int | None = None) -> list[SpaceSeasonSummary]:
        "Get SpaceScore season history # Get recent SpaceScore seasons for a space"
        request_path = "/api/v1/spaces/{id}/xp/history"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "limit", limit, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SpaceSeasonSummary],
        )

    async def get_space_score_leaderboard_endpoint(self, id: str, *, limit: int | None = None) -> list[LeaderboardEntry]:
        "Get SpaceScore leaderboard # Get the current SpaceScore leaderboard for a space"
        request_path = "/api/v1/spaces/{id}/xp/leaderboard"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "limit", limit, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[LeaderboardEntry],
        )

    async def get_space_score_member_summary_endpoint(self, id: str, member_id: str) -> SpaceMemberSummary:
        "Get SpaceScore member summary # Get the current SpaceScore summary for a space member"
        request_path = "/api/v1/spaces/{id}/xp/members/{memberId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{memberId}", quote(_query_value(member_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceMemberSummary,
        )

    async def get_space_score_season_endpoint(self, id: str) -> SpaceSeasonSummary:
        "Get SpaceScore season summary # Get the current SpaceScore season summary for a space"
        request_path = "/api/v1/spaces/{id}/xp/season"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceSeasonSummary,
        )

    async def get_spaces_endpoint(self) -> list[Space]:
        "Get all spaces # Get all spaces"
        request_path = "/api/v1/spaces/"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Space],
        )

    async def invite_user_to_space_endpoint(self, id: str, *, body: InvitationRequest | None = None) -> Invitation:
        "Invite # Invite a user to a space"
        request_path = "/api/v1/spaces/{id}/invite"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Invitation,
        )

    async def leave_space_endpoint(self, id: str, *, body: LeaveSpaceRequest | None = None) -> None:
        "Leave space # Leave space"
        request_path = "/api/v1/spaces/{id}/leave"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def open_invitation_to_space_endpoint(self, id: str) -> Invitation:
        "Open invitation # Creates a open invitation to a space to use in for example a qr-code"
        request_path = "/api/v1/spaces/{id}/open-invitation"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Invitation,
        )

    async def update_space_endpoint(self, id: str, *, body: Space | None = None) -> Space:
        "Update a space by id # Update a space by id"
        request_path = "/api/v1/spaces/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Space,
        )

    async def update_space_member_endpoint(self, id: str, member_id: str, *, body: UpdateSpaceMemberRequest | None = None) -> SpaceMember:
        "Update space member # Update a space member"
        request_path = "/api/v1/spaces/{id}/members/{memberId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{memberId}", quote(_query_value(member_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceMember,
        )

    async def update_space_reward_claim_endpoint(self, id: str, claim_id: str, *, body: UpdateSpaceRewardClaimRequest | None = None) -> SpaceRewardClaim:
        "Update reward claim # Approve, reject, or fulfill a reward claim"
        request_path = "/api/v1/spaces/{id}/xp/rewards/claims/{claimId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{claimId}", quote(_query_value(claim_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceRewardClaim,
        )

    async def update_space_reward_endpoint(self, id: str, reward_id: str, *, body: UpdateSpaceRewardRequest | None = None) -> SpaceReward:
        "Update space reward # Update a reward definition"
        request_path = "/api/v1/spaces/{id}/xp/rewards/{rewardId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{rewardId}", quote(_query_value(reward_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceReward,
        )

    async def update_space_user_role_endpoint(self, id: str, *, body: ChangeSpaceUserRoleRequest | None = None) -> SpaceUserLink:
        "Update a user's role in a space # Update a user's role in a space"
        request_path = "/api/v1/spaces/{id}/role"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=SpaceUserLink,
        )

    async def users_in_space_endpoint(self, id: str) -> list[UserResponse]:
        "Users in space # Users in space"
        request_path = "/api/v1/spaces/{id}/users"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[UserResponse],
        )


class SpacesApi:
    "Spaces endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def koble_permissions_endpoint(self) -> KobleSpacesResponse:
        "What the caller may do with Koble objects in each of their households, so a client can offer only the actions that will succeed. The same answer as GET /api/v1/spaces, at a path that does not collide with Famn's own spaces service."
        request_path = "/api/v1/koble/permissions"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleSpacesResponse,
        )


class StorageApi:
    "Storage endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_storage_group_endpoint(self, *, body: CreateStorageGroupRequest | None = None) -> StorageGroup:
        "Create a new storage group # Create a new storage group"
        request_path = "/api/v1/files/storage/groups"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StorageGroup,
        )

    async def create_storage_plan_endpoint(self, *, body: CreateStoragePlanRequest | None = None) -> StoragePlan:
        "Create a new storage plan # Create a new storage plan"
        request_path = "/api/v1/files/storage/plans"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StoragePlan,
        )

    async def delete_storage_group_endpoint(self, id: str) -> None:
        "Delete a storage group by id # Delete a storage group by id"
        request_path = "/api/v1/files/storage/groups/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_storage_plan_endpoint(self, id: str) -> None:
        "Delete a storage plan by id # Delete a storage plan by id"
        request_path = "/api/v1/files/storage/plans/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_storage_group_by_groupable_id_and_type_endpoint(self, groupable_id: str, groupable_type: str) -> StorageGroup:
        "Get a storage group by groupable ID and type # Get a storage group by groupable ID and type"
        request_path = "/api/v1/files/storage/groups/find-by-groupable-id-and-type"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "groupable_id", groupable_id, "")
        _add_query(request_query, "groupable_type", groupable_type, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StorageGroup,
        )

    async def get_storage_group_endpoint(self, id: str) -> StorageGroup:
        "Get a storage group by id # Get a storage group by id"
        request_path = "/api/v1/files/storage/groups/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StorageGroup,
        )

    async def get_storage_groups_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> StorageGroupPaginateResponse:
        "Get all storage groups # Get all storage groups"
        request_path = "/api/v1/files/storage/groups"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StorageGroupPaginateResponse,
        )

    async def get_storage_plan_endpoint(self, id: str) -> StoragePlan:
        "Get a storage plan by id # Get a storage plan by id"
        request_path = "/api/v1/files/storage/plans/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StoragePlan,
        )

    async def get_storage_plans_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> StoragePlanPaginateResponse:
        "Get all storage plans # Get all storage plans"
        request_path = "/api/v1/files/storage/plans"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StoragePlanPaginateResponse,
        )

    async def update_storage_group_endpoint(self, id: str, *, body: StorageGroup | None = None) -> StorageGroup:
        "Update a storage group by id # Update a storage group by id"
        request_path = "/api/v1/files/storage/groups/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StorageGroup,
        )

    async def update_storage_plan_endpoint(self, id: str, *, body: StoragePlan | None = None) -> StoragePlan:
        "Update a storage plan by id # Update a storage plan by id"
        request_path = "/api/v1/files/storage/plans/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=StoragePlan,
        )


class StoreApi:
    "Store endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def store_get_nearby_endpoint(self, *, body: GetNearbyRequest | None = None) -> list[Store]:
        "Get stores nearby # Get stores nearby"
        request_path = "/api/v1/shopping/store/get-nearby"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Store],
        )


class SubscriptionApi:
    "Subscription endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def get_subscription_campaigns_endpoint(self, platform: str) -> list[SubscriptionCampaignResponse]:
        "Get subscription campaigns # Get subscription campaigns"
        request_path = "/api/v1/access/subscriptions/campaigns"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "platform", platform, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SubscriptionCampaignResponse],
        )

    async def get_subscription_products_endpoint(self, app_short_name: str, product_store: str) -> list[SubscriptionProduct]:
        "Get subscription products # Get subscription products by app and product store"
        request_path = "/api/v1/access/subscriptions/products"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app_short_name", app_short_name, "")
        _add_query(request_query, "product_store", product_store, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[SubscriptionProduct],
        )

    async def get_subscriptions_endpoint(self) -> list[AccountSubscription]:
        "Get user subscriptions # Get user subscriptions"
        request_path = "/api/v1/access/subscriptions"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[AccountSubscription],
        )

    async def verify_purchase_endpoint(self, *, body: VerifyPurchaseRequest | None = None) -> list[AccountPurchase]:
        "Verify IAP purchase # Verify IAP purchase"
        request_path = "/api/v1/access/subscriptions/verify-purchase"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[AccountPurchase],
        )


class TasksApi:
    "Tasks endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_task_item_category_endpoint(self, *, body: CreateTaskItemCategoryRequest | None = None) -> TaskItemCategory:
        "Create a new task item category # Create a new task item category"
        request_path = "/api/v1/tasks/categories"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskItemCategory,
        )

    async def create_task_item_endpoint(self, task_list_id: str, *, body: CreateTaskItemRequest | None = None) -> TaskItem:
        "Create a new task item # Create a new task item"
        request_path = "/api/v1/tasks/{task_list_id}/items"
        request_path = request_path.replace("{task_list_id}", quote(_query_value(task_list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskItem,
        )

    async def create_task_list_endpoint(self, *, body: CreateTaskListRequest | None = None) -> TaskList:
        "Create a new task list # Create a new task list"
        request_path = "/api/v1/tasks"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskList,
        )

    async def delete_task_item_category_endpoint(self, id: str) -> None:
        "Delete a task item category by id # Delete a task item category by id"
        request_path = "/api/v1/tasks/categories/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_task_item_endpoint(self, id: str, task_list_id: str) -> None:
        "Delete a task item by id # Delete a task item by id"
        request_path = "/api/v1/tasks/{task_list_id}/items/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{task_list_id}", quote(_query_value(task_list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_task_list_endpoint(self, id: str) -> None:
        "Delete a task list by id # Delete a task list by id"
        request_path = "/api/v1/tasks/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_ai_chore_generator_endpoint(self, prompt: str) -> list[TaskItem]:
        "Use AI to generate example chores based on user prompt # Use AI to generate example chores based on user prompt"
        request_path = "/api/v1/tasks/items/ai-chore-generator"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "prompt", prompt, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[TaskItem],
        )

    async def get_example_tasks_endpoint(self) -> list[TaskItem]:
        "Get example task items # Get example task items"
        request_path = "/api/v1/tasks/items/example"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[TaskItem],
        )

    async def get_task_item_categories_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None) -> TaskItemCategoryPaginateResponse:
        "Get all task item categories # Get all task item categories"
        request_path = "/api/v1/tasks/categories"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskItemCategoryPaginateResponse,
        )

    async def get_task_item_category_endpoint(self, id: str) -> TaskItemCategory:
        "Get a task item category by id # Get a task item category by id"
        request_path = "/api/v1/tasks/categories/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskItemCategory,
        )

    async def get_task_item_endpoint(self, id: str, task_list_id: str) -> TaskItem:
        "Get a task item by id # Get a task item by id"
        request_path = "/api/v1/tasks/{task_list_id}/items/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{task_list_id}", quote(_query_value(task_list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskItem,
        )

    async def get_task_item_history_by_space_endpoint(self, space_id: str, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, from_date: str | None = None, to_date: str | None = None) -> TaskItemHistoryPaginateResponse:
        "Get task item history by space # Get task item history by space"
        request_path = "/api/v1/tasks/items/history-by-space"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "from_date", from_date, "")
        _add_query(request_query, "to_date", to_date, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskItemHistoryPaginateResponse,
        )

    async def get_task_items_endpoint(self, task_list_id: str, *, filter: str | None = None, completed: bool | None = None, next: bool | None = None) -> list[TaskItem]:
        "Get all task items # Get all task items"
        request_path = "/api/v1/tasks/{task_list_id}/items"
        request_path = request_path.replace("{task_list_id}", quote(_query_value(task_list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "completed", completed, "")
        _add_query(request_query, "next", next, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[TaskItem],
        )

    async def get_task_list_endpoint(self, id: str) -> TaskList:
        "Get a task list by id # Get a task list by id"
        request_path = "/api/v1/tasks/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskList,
        )

    async def get_task_list_members_endpoint(self, id: str) -> list[TaskListUserLink]:
        "Get all task list members # Get all task list members"
        request_path = "/api/v1/tasks/{id}/members"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[TaskListUserLink],
        )

    async def get_task_lists_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None, task_type: str | None = None) -> TaskListPaginateResponse:
        "Get all task lists # Get all task lists"
        request_path = "/api/v1/tasks"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "task_type", task_type, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskListPaginateResponse,
        )

    async def get_user_tasks_endpoint(self, *, filter: str | None = None) -> list[TaskItem]:
        "Get user's task items # Get user's task items"
        request_path = "/api/v1/tasks/items/mine"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "filter", filter, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[TaskItem],
        )

    async def log_task_item_done_endpoint(self, id: str, task_list_id: str, *, skip: bool | None = None, executing_user_id: str | None = None, time_of_completion: str | None = None, lat: float | None = None, lng: float | None = None) -> TaskItem:
        "Log a task item as done # Log a task item as done"
        request_path = "/api/v1/tasks/{task_list_id}/items/{id}/done"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{task_list_id}", quote(_query_value(task_list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "skip", skip, "")
        _add_query(request_query, "executing_user_id", executing_user_id, "")
        _add_query(request_query, "time_of_completion", time_of_completion, "")
        _add_query(request_query, "lat", lat, "")
        _add_query(request_query, "lng", lng, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskItem,
        )

    async def mute_task_list_endpoint(self, id: str, *, mute_until: str | None = None) -> None:
        "Mute task list notifications # Mute task list notifications"
        request_path = "/api/v1/tasks/{id}/mute"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "mute_until", mute_until, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def set_should_notify_task_list_endpoint(self, id: str, should_notify: bool) -> None:
        "Set should notify setting for task list notifications # Set should notify setting for task list notifications"
        request_path = "/api/v1/tasks/{id}/set-should-notify"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "should_notify", should_notify, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def un_mute_task_list_endpoint(self, id: str) -> None:
        "Un mute task list notifications # Un mute task list notifications"
        request_path = "/api/v1/tasks/{id}/un-mute"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def update_task_item_category_endpoint(self, id: str, *, body: TaskItemCategory | None = None) -> TaskItemCategory:
        "Update a task item category by id # Update a task item category by id"
        request_path = "/api/v1/tasks/categories/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskItemCategory,
        )

    async def update_task_item_endpoint(self, id: str, task_list_id: str, *, body: TaskItem | None = None) -> TaskItem:
        "Update a task item by id # Update a task item by id"
        request_path = "/api/v1/tasks/{task_list_id}/items/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{task_list_id}", quote(_query_value(task_list_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskItem,
        )

    async def update_task_list_endpoint(self, id: str, *, body: TaskList | None = None) -> TaskList:
        "Update a task list by id # Update a task list by id"
        request_path = "/api/v1/tasks/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TaskList,
        )

    async def update_task_list_members_endpoint(self, id: str, *, body: list[TaskListUserLink] | None = None) -> list[TaskListUserLink]:
        "Update task list members # Update task list members"
        request_path = "/api/v1/tasks/{id}/members"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PUT",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[TaskListUserLink],
        )


class TicketApi:
    "Ticket endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_ticket_endpoint(self, *, body: CreateTicketRequest | None = None) -> Ticket:
        "Create a new support ticket # Create a new support ticket"
        request_path = "/api/v1/supporting/tickets"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Ticket,
        )

    async def get_ticket_endpoint(self, ticket_id: str) -> Ticket:
        "Get support ticket by id # Get support ticket by id"
        request_path = "/api/v1/supporting/tickets/{ticket_id}"
        request_path = request_path.replace("{ticket_id}", quote(_query_value(ticket_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Ticket,
        )

    async def get_tickets_endpoint(self, *, app_name: str | None = None, status: str | None = None, limit: int | None = None, include_messages: bool | None = None) -> list[Ticket]:
        "Get support tickets for app # Get support tickets for app"
        request_path = "/api/v1/supporting/tickets"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "app-name", app_name, "")
        _add_query(request_query, "status", status, "")
        _add_query(request_query, "limit", limit, "")
        _add_query(request_query, "include_messages", include_messages, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[Ticket],
        )

    async def postmark_inbound_ticket_endpoint(self) -> None:
        "Postmark inbound webhook for ticket replies # Postmark inbound webhook for ticket replies"
        request_path = "/api/v1/supporting/tickets/postmark/inbound"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=None,
        )

    async def reply_ticket_endpoint(self, ticket_id: str, *, body: ReplyTicketRequest | None = None) -> TicketMessage:
        "Reply to an existing ticket # Reply to an existing ticket"
        request_path = "/api/v1/supporting/tickets/{ticket_id}/reply"
        request_path = request_path.replace("{ticket_id}", quote(_query_value(ticket_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TicketMessage,
        )

    async def update_ticket_status_endpoint(self, ticket_id: str, *, body: UpdateTicketStatusRequest | None = None) -> Ticket:
        "Update status on an existing ticket # Update status on an existing ticket"
        request_path = "/api/v1/supporting/tickets/{ticket_id}/status"
        request_path = request_path.replace("{ticket_id}", quote(_query_value(ticket_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=Ticket,
        )


class TinyURLApi:
    "TinyURL endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def create_tiny_url_endpoint(self, *, body: CreateTinyUrlRequest | None = None) -> TinyURL:
        "Create a new tiny url # Create a new tiny url"
        request_path = "/api/v1/tinyqr/tinyURL"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=TinyURL,
        )

    async def get_tiny_url_endpoint(self) -> None:
        "Get tiny url and redirects to the original url # Get tiny url and redirects to the original url"
        request_path = "/u/{short_url}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=None,
        )

    async def get_tiny_url_qrcode_endpoint(self) -> None:
        "Get Tiny Url Qr Code png # Get Tiny Url Qr Code png"
        request_path = "/api/v1/tinyqr/tinyURL/qr/{short_url}"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=[],
            response_type=None,
        )


class TrailersApi:
    "Trailers endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def archive_trailer_endpoint(self, id: str) -> KobleTrailer:
        "Remove from the household: archives the object, which drops live placements elsewhere and stops future provider sync. Historical snapshots and evidence are untouched, and it can be brought back. Permanent removal is DELETE. Idempotent — archiving an archived object succeeds."
        request_path = "/api/v1/trailers/{id}/archive"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleTrailer,
        )

    async def create_trailer_endpoint(self, body: CreateTrailerRequest) -> KobleTrailer:
        "Register a trailer manually; weight-critical fields get evidence rows."
        request_path = "/api/v1/trailers"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleTrailer,
        )

    async def delete_trailer_endpoint(self, id: str) -> None:
        "Soft-delete a trailer."
        request_path = "/api/v1/trailers/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_trailer_image_endpoint(self, id: str, image_id: str) -> None:
        "Remove an image from the trailer."
        request_path = "/api/v1/trailers/{id}/images/{imageId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{imageId}", quote(_query_value(image_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_trailer_endpoint(self, id: str) -> KobleTrailer:
        "Get one trailer with its equipment list."
        request_path = "/api/v1/trailers/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleTrailer,
        )

    async def list_trailer_evidence_endpoint(self, id: str) -> None:
        "List the provenance history per field."
        request_path = "/api/v1/trailers/{id}/evidence"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def list_trailer_images_endpoint(self, id: str) -> list[KobleEntityImage]:
        "List the trailer's images in gallery order."
        request_path = "/api/v1/trailers/{id}/images"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[KobleEntityImage],
        )

    async def list_trailers_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None, include_candidates: bool | None = None, collection_role: str | None = None) -> TrailerPaginateResponse:
        "List the account's trailers with filtering and pagination."
        request_path = "/api/v1/trailers"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "include_candidates", include_candidates, "")
        _add_query(request_query, "collection_role", collection_role, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=TrailerPaginateResponse,
        )

    async def patch_trailer_endpoint(self, id: str, body: PatchTrailerRequest) -> KobleTrailer:
        "Patch trailer fields; corrections are recorded as user-override evidence."
        request_path = "/api/v1/trailers/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleTrailer,
        )

    async def set_trailer_scope_endpoint(self, id: str, body: KobleMoveScopeRequest) -> KobleTrailer:
        "Share, transfer or unshare a trailer. spaceId set moves it into that space (needs koble.create there); spaceId null makes it private (needs koble.manage_sharing in its current space)."
        request_path = "/api/v1/trailers/{id}/scope"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleTrailer,
        )

    async def trailer_registry_lookup_endpoint(self, body: KobleRegistryLookupRequest) -> KobleImportJob:
        "Create a reviewable trailer draft from a registry lookup."
        request_path = "/api/v1/trailers/lookup"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleImportJob,
        )

    async def upload_trailer_image_endpoint(self, id: str, file: FileValue, *, alt_text: str | None = None) -> KobleEntityImage:
        "Upload an image (multipart field \"file\", optional \"altText\") and attach it to the trailer."
        request_path = "/api/v1/trailers/{id}/images"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_files["file"] = file
        if alt_text is not None:
            request_form["altText"] = alt_text
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=KobleEntityImage,
        )


class VehiclesApi:
    "Vehicles endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def apply_vehicle_model_reference_endpoint(self, id: str, body: KobleApplyModelReferenceRequest) -> KobleVehicle:
        "Fill missing vehicle fields from a selected model reference. Existing values are preserved and applied fields receive medium-confidence reference evidence."
        request_path = "/api/v1/vehicles/{id}/enrich-reference"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicle,
        )

    async def archive_vehicle_endpoint(self, id: str) -> KobleVehicle:
        "Remove from the household: archives the object, which drops live placements elsewhere and stops future provider sync. Historical snapshots and evidence are untouched, and it can be brought back. Permanent removal is DELETE. Idempotent — archiving an archived object succeeds."
        request_path = "/api/v1/vehicles/{id}/archive"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicle,
        )

    async def create_vehicle_endpoint(self, body: CreateVehicleRequest) -> KobleVehicle:
        "Register a vehicle manually; weight-critical fields get evidence rows."
        request_path = "/api/v1/vehicles"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicle,
        )

    async def delete_vehicle_endpoint(self, id: str) -> None:
        "Soft-delete a vehicle (archive via PATCH status=archived instead to keep it visible)."
        request_path = "/api/v1/vehicles/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def delete_vehicle_image_endpoint(self, id: str, image_id: str) -> None:
        "Remove an image from the vehicle."
        request_path = "/api/v1/vehicles/{id}/images/{imageId}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_path = request_path.replace("{imageId}", quote(_query_value(image_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def get_vehicle_endpoint(self, id: str) -> KobleVehicle:
        "Get one vehicle with its energy sources."
        request_path = "/api/v1/vehicles/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicle,
        )

    async def list_vehicle_evidence_endpoint(self, id: str) -> None:
        "List the provenance history (source, confidence, original text) per field."
        request_path = "/api/v1/vehicles/{id}/evidence"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=None,
        )

    async def list_vehicle_images_endpoint(self, id: str) -> list[KobleEntityImage]:
        "List the vehicle's images in gallery order."
        request_path = "/api/v1/vehicles/{id}/images"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=list[KobleEntityImage],
        )

    async def list_vehicles_endpoint(self, *, page: int | None = None, page_size: int | None = None, order_by: str | None = None, order: str | None = None, filter: str | None = None, space_id: str | None = None, include_candidates: bool | None = None, collection_role: str | None = None) -> VehiclePaginateResponse:
        "List the account's vehicles with filtering and pagination."
        request_path = "/api/v1/vehicles"
        request_query: list[tuple[str, str]] = []
        _add_query(request_query, "page", page, "")
        _add_query(request_query, "page_size", page_size, "")
        _add_query(request_query, "order_by", order_by, "")
        _add_query(request_query, "order", order, "")
        _add_query(request_query, "filter", filter, "")
        _add_query(request_query, "space_id", space_id, "")
        _add_query(request_query, "include_candidates", include_candidates, "")
        _add_query(request_query, "collection_role", collection_role, "")
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=VehiclePaginateResponse,
        )

    async def patch_vehicle_endpoint(self, id: str, body: PatchVehicleRequest) -> KobleVehicle:
        "Patch vehicle fields; corrections are recorded as user-override evidence."
        request_path = "/api/v1/vehicles/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "PATCH",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicle,
        )

    async def set_vehicle_scope_endpoint(self, id: str, body: KobleMoveScopeRequest) -> KobleVehicle:
        "Share, transfer or unshare a vehicle. spaceId set moves it into that space (needs koble.create there); spaceId null makes it private (needs koble.manage_sharing in its current space)."
        request_path = "/api/v1/vehicles/{id}/scope"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicle,
        )

    async def upload_vehicle_image_endpoint(self, id: str, file: FileValue, *, alt_text: str | None = None) -> KobleEntityImage:
        "Upload an image (multipart field \"file\", optional \"altText\") and attach it to the vehicle."
        request_path = "/api/v1/vehicles/{id}/images"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_files["file"] = file
        if alt_text is not None:
            request_form["altText"] = alt_text
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="multipart/form-data",
            auth_names=["Bearer"],
            response_type=KobleEntityImage,
        )

    async def vehicle_registry_enrich_endpoint(self, id: str, *, body: KobleRegistryEnrichRequest | None = None) -> KobleVehicle:
        "Enrich an existing vehicle with verified registry data. The body may name an identifier; empty means the vehicle's stored registration number. Registry values win over listing values for technical fields; explicit user overrides and non-registry fields are preserved."
        request_path = "/api/v1/vehicles/{id}/enrich"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicle,
        )

    async def vehicle_registry_lookup_endpoint(self, body: KobleRegistryLookupRequest) -> KobleImportJob:
        "Create a reviewable vehicle draft from Norwegian Vegvesen, Dutch RDW or US NHTSA vPIC. countryCode defaults to NO; US vPIC is manufacturer VIN data, not a state registration record."
        request_path = "/api/v1/vehicles/lookup"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleImportJob,
        )


class KobleApi:
    "koble endpoints."
    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client

    async def koble_smartcar_begin_connect(self, body: KobleSmartcarBeginConnectRequest) -> KobleSmartcarConnectSession:
        "Reserves a vehicle seat and returns the provider consent URL."
        request_path = "/api/v1/smartcar/connections"
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        request_body = body
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleSmartcarConnectSession,
        )

    async def koble_smartcar_disconnect(self, id: str) -> KobleSmartcarConnection:
        "Ends a provider connection. Works with the integration switched off."
        request_path = "/api/v1/smartcar/connections/{id}"
        request_path = request_path.replace("{id}", quote(_query_value(id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "DELETE",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleSmartcarConnection,
        )

    async def koble_smartcar_refresh_telemetry(self, vehicle_id: str) -> KobleVehicleTelemetrySnapshot:
        "Fetches a fresh reading. Rate-limited per vehicle; a call inside the cooldown returns the stored reading unchanged rather than failing."
        request_path = "/api/v1/smartcar/vehicles/{vehicleId}/telemetry/refresh"
        request_path = request_path.replace("{vehicleId}", quote(_query_value(vehicle_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "POST",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicleTelemetrySnapshot,
        )

    async def koble_smartcar_telemetry(self, vehicle_id: str) -> KobleVehicleTelemetrySnapshot:
        "The latest normalised reading. Does not contact the provider."
        request_path = "/api/v1/smartcar/vehicles/{vehicleId}/telemetry"
        request_path = request_path.replace("{vehicleId}", quote(_query_value(vehicle_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicleTelemetrySnapshot,
        )

    async def koble_smartcar_vehicle_state(self, vehicle_id: str) -> KobleVehicleSmartcarState:
        "Whether this vehicle is connected, and its latest reading. Does not contact the provider. Answers 200 with nulls rather than 404 — \"not connected\" is an answer, not a missing resource."
        request_path = "/api/v1/smartcar/vehicles/{vehicleId}"
        request_path = request_path.replace("{vehicleId}", quote(_query_value(vehicle_id), safe=""))
        request_query: list[tuple[str, str]] = []
        request_headers: dict[str, str] = {}
        request_body: Any = None
        request_form: dict[str, Any] = {}
        request_files: dict[str, FileValue] = {}
        return await self.api_client.request(
            "GET",
            request_path,
            query=request_query,
            headers=request_headers,
            body=request_body,
            form=request_form,
            files=request_files,
            content_type="application/json",
            auth_names=["Bearer"],
            response_type=KobleVehicleSmartcarState,
        )


__all__ = ["AccountApi", "AccountScoreApi", "ApplicationApi", "AttachmentApi", "AuthenticateApi", "CalcApi", "CalendarApi", "CampaignApi", "CaravansApi", "ChangelogApi", "ChatApi", "ClubCardApi", "ContactApi", "CookbookApi", "DeviceApi", "EntryApi", "FAQApi", "FeatureApi", "FileApi", "HoldingsApi", "ImageApi", "ImportsApi", "InvitationApi", "ListApi", "ListItemApi", "LocalesApi", "MealApi", "MealPlannerApi", "MetadataApi", "NewsletterApi", "NotificationApi", "PlacementsApi", "ProductApi", "ProductCategoryApi", "PropertyApi", "ReferralApi", "SenderApi", "SessionApi", "SpaceApi", "SpacesApi", "StorageApi", "StoreApi", "SubscriptionApi", "TasksApi", "TicketApi", "TinyURLApi", "TrailersApi", "VehiclesApi", "KobleApi", ]

